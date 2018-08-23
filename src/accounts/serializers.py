import re
import os
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import SetPasswordForm
from django.conf import settings
from django.utils.module_loading import import_string

from .utils import sync_sso

from rest_framework import serializers, exceptions
from allauth.account.forms import ResetPasswordForm, default_token_generator

from allauth.account.utils import send_email_confirmation, user_pk_to_url_str
from django.contrib.sites.shortcuts import get_current_site

from library.serializers import ProfileSerializer
from library.models import Track

from allauth.account.forms import UserTokenForm
from allauth.account.adapter import get_adapter

from allauth.utils import email_address_exists
from allauth.account.models import EmailAddress

from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.utils import setup_user_email

from avatar.models import Avatar
from avatar.signals import avatar_updated
from django.template.defaultfilters import filesizeformat

from rest_framework.authtoken.models import Token

UserModel = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def _validate_username_email(self, username, email, password):
        user = None

        if email and password:
            user = authenticate(email=email, password=password)
        elif username and password:
            user = authenticate(username=username, password=password)
        else:
            msg = _('Must include either "username" or "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')

        user = self._validate_username_email(username, email, password)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # Is the email verified?
        email_address = user.emailaddress_set.get(email=user.email)
        if not email_address.verified:
            raise exceptions.PermissionDenied('not verified')

        attrs['user'] = user
        return attrs


class PasswordResetSerializer(serializers.Serializer):

    email = serializers.EmailField()

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if not email_address_exists(email):
            raise serializers.ValidationError(_('The e-mail address is not assigned '
                                                'to any user account'))
        return email

    def save(self, *args, **kwargs):
        request = self.context.get('request')

        current_site = get_current_site(request)
        email = self.validated_data['email']

        user = UserModel.objects.get(email__iexact=email)

        token_generator = kwargs.get(
            'token_generator', default_token_generator)
        temp_key = token_generator.make_token(user)

        path = f'/reset-password/{user_pk_to_url_str(user)}/{temp_key}'
        url = settings.SPA_BASE_URL + path
        context = {'current_site': current_site,
                   'user': user,
                   'password_reset_url': url,
                   'request': request}

        get_adapter().send_mail(
            'account/email/password_reset_key',
            email,
            context)

        return email


class ResendConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()

    password_reset_form_class = ResetPasswordForm

    def validate(self, attrs):
        self.reset_form = self.password_reset_form_class(
            data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)

        return attrs

    def save(self):
        request = self.context.get('request')
        User = get_user_model()
        email = self.reset_form.cleaned_data['email']
        user = User.objects.get(email__iexact=email)
        send_email_confirmation(request, user, True)
        return email


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)
    uid = serializers.CharField()
    key = serializers.CharField()

    def validate_new_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, attrs):
        self.user_token_form = UserTokenForm(
            data={'uidb36': attrs['uid'], 'key': attrs['key']})

        if not self.user_token_form.is_valid():
            raise serializers.ValidationError(_("التوكن غير صالح"))

        if attrs['new_password1'] != attrs['new_password2']:
            raise serializers.ValidationError(
                _('The two password fields did not match.'))

        self.password = attrs['new_password1']

        return attrs

    def save(self):
        user = self.user_token_form.reset_user
        get_adapter().set_password(user, self.password)
        return user


class UserDetailsSerializer(serializers.ModelSerializer):
    email_status = serializers.SerializerMethodField()
    avatar_url = serializers.SerializerMethodField()
    profile = ProfileSerializer()
    avatar = serializers.ImageField(write_only=True, required=False)
    name = serializers.CharField(source='first_name',
                                 max_length=100,
                                 min_length=5)

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'email_status',
                  'name', 'profile', 'avatar', 'avatar_url')

    def get_email_status(self, obj):
        email_address = EmailAddress.objects.get(user=obj)
        return email_address.verified

    def get_avatar_url(self, obj, size=settings.AVATAR_DEFAULT_SIZE):
        for provider_path in settings.AVATAR_PROVIDERS:
            provider = import_string(provider_path)
            avatar_url = provider.get_avatar_url(obj, size)
            if avatar_url:
                return avatar_url

    def validate_name(self, name):
        pattern = '^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ðء-ي]+ [a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ðء-ي]+[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ðء-ي ]*$'
        compiler = re.compile(pattern)
        if not compiler.match(name):
            raise serializers.ValidationError(
                _("تأكد أن الإسم الكامل لا يحتوي الا على حروف و مسافات."))

        return name

    def validate_avatar(self, avatar):
        if settings.AVATAR_ALLOWED_FILE_EXTS:
            root, ext = os.path.splitext(avatar.name.lower())
            if ext not in settings.AVATAR_ALLOWED_FILE_EXTS:
                valid_exts = ', '.join(settings.AVATAR_ALLOWED_FILE_EXTS)
                error = _("لا يمكن استعمال %(ext)s .. الامتدادات الصالحة:%(valid_exts_list)s")
                raise serializers.ValidationError(error %
                                                  {'ext': ext,
                                                   'valid_exts_list': valid_exts})

        if avatar.size > settings.AVATAR_MAX_SIZE:
            error = _("الملف كبير جدا %(size)s, أفصى حد هو:%(max_valid_size)s")

            raise serializers.ValidationError(error % {
                'size': filesizeformat(avatar.size),
                'max_valid_size': filesizeformat(settings.AVATAR_MAX_SIZE)
            })

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and email_address_exists(email, exclude_user=self.context.get('request').user):
            raise serializers.ValidationError(
                _('A user is already registered with this e-mail address.'))
        return email

    def update(self, instance, validated_data):
        request = self.context.get('request')

        profile = validated_data.get('profile', None)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        if profile:
            new_track = profile.get('track')
            track = Track.objects.get(slug=new_track.slug)
            is_track_updated = instance.profile.track != new_track
            instance.profile.track = track
            instance.profile.last_opened_lesson = profile.get(
                'last_opened_lesson', instance.profile.last_opened_lesson)
            if is_track_updated:
                instance.profile.last_opened_lesson = None

        email = validated_data.get('email', None)
        if email and email != instance.email:
            adapter = get_adapter()
            adapter.send_mail('account/email/email_change', instance.email, {})
            email_address = EmailAddress.objects.get(
                user=instance, verified=True)
            email_address.change(request, email, True)
            instance.email = email

        if 'avatar' in request.FILES:
            avatar = Avatar(user=instance, primary=True)
            image_file = request.FILES['avatar']
            avatar.avatar.save(image_file.name, image_file)
            avatar.save()
            avatar_updated.send(sender=Avatar, user=instance, avatar=avatar)

        instance.save()

        sync_sso(instance)

        return instance


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128)
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)

    set_password_form_class = SetPasswordForm

    def __init__(self, *args, **kwargs):
        self.old_password_field_enabled = getattr(
            settings, 'OLD_PASSWORD_FIELD_ENABLED', False
        )
        self.logout_on_password_change = getattr(
            settings, 'LOGOUT_ON_PASSWORD_CHANGE', False
        )
        super(PasswordChangeSerializer, self).__init__(*args, **kwargs)

        if not self.old_password_field_enabled:
            self.fields.pop('old_password')

        self.request = self.context.get('request')
        self.user = getattr(self.request, 'user', None)

    def validate_old_password(self, value):
        invalid_password_conditions = (
            self.old_password_field_enabled,
            self.user,
            not self.user.check_password(value)
        )

        if all(invalid_password_conditions):
            raise serializers.ValidationError('Invalid password')
        return value

    def validate(self, attrs):
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )

        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        return attrs

    def save(self):
        self.set_password_form.save()
        if not self.logout_on_password_change:
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(self.request, self.user)


class TokenSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer()

    class Meta:
        model = Token
        fields = ('key', 'user')


# Registration

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    name = serializers.CharField(
        max_length=100,
        min_length=5,
        required=True
    )

    def validate_name(self, name):
        pattern = '^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ðء-ي]+ [a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ðء-ي]+[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ðء-ي ]*$'
        compiler = re.compile(pattern)
        if not compiler.match(name):
            raise serializers.ValidationError(
                _("تأكد أن الإسم الكامل لا يحتوي الا على حروف و مسافات."))

        return name

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        sync_sso(user)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('name', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user


class VerifyEmailSerializer(serializers.Serializer):
    key = serializers.CharField()