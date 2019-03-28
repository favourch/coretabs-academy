import re
import os
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import SetPasswordForm
from django.conf import settings
from django.utils.module_loading import import_string

from rest_framework import serializers, exceptions

from .signals import user_updated

from .models import EmailAddress, Account
from .utils import send_password_reset_mail

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.password_validation import validate_password

from avatar.models import Avatar
from avatar.signals import avatar_updated
from django.template.defaultfilters import filesizeformat

from rest_framework.authtoken.models import Token

from .tokens import confirm_email_token_generator
from django.contrib.auth.tokens import default_token_generator as password_reset_token_generator
from django.utils.http import base36_to_int, int_to_base36

from django.contrib.auth import update_session_auth_hash

from library.models import Track

User = get_user_model()


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
        email_address = EmailAddress.objects.get_primary(user)
        if not email_address.verified:
            raise exceptions.PermissionDenied('not verified')

        attrs['user'] = user
        return attrs


class AccountSerializer(serializers.ModelSerializer):
    track = serializers.SlugRelatedField(
        slug_field='slug', read_only=False, queryset=Track.objects)
    last_opened_workshop_slug = serializers.SerializerMethodField()
    last_opened_module_slug = serializers.SerializerMethodField()
    last_opened_lesson_slug = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ('track',
                  'last_opened_lesson',
                  'last_opened_workshop_slug',
                  'last_opened_module_slug',
                  'last_opened_lesson_slug',)

    def get_last_opened_workshop_slug(self, obj):
        result = None
        if obj.last_opened_lesson and obj.track:
            try:
                result = obj.last_opened_lesson.module.workshops.filter(
                    tracks__id=obj.track.id).first().slug
            except AttributeError:
                result = None
        return result

    def get_last_opened_module_slug(self, obj):
        result = None
        if obj.last_opened_lesson:
            result = obj.last_opened_lesson.module.slug
        return result

    def get_last_opened_lesson_slug(self, obj):
        result = None
        if obj.last_opened_lesson:
            result = obj.last_opened_lesson.slug
        return result


class UserDetailsSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()
    batch_status = serializers.SerializerMethodField()
    account = AccountSerializer()
    avatar = serializers.ImageField(write_only=True, required=False)
    name = serializers.CharField(source='first_name',
                                 max_length=100,
                                 min_length=5)

    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'account',
                  'avatar', 'avatar_url', 'batch_status')

    def get_batch_status(self, obj):
        return obj.has_perm('accounts.access_workshops')

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
                _("تأكد أن تدخل اسمك الكامل (الاسم واللقب) وأنه لا يحتوي إلا على الحروف و المسافات, سيستعمل اسمك في إنتاج شهادتك."))

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
        if email != self.instance.email and User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError(
                _("A user is already registered with this e-mail address."))
        return email

    def _update_account(self, instance, account):
        new_track = account.get('track')
        track = Track.objects.get(slug=new_track.slug)
        is_track_updated = instance.account.track != new_track
        instance.account.track = track
        instance.account.last_opened_lesson = account.get(
            'last_opened_lesson', instance.account.last_opened_lesson)
        if is_track_updated:
            instance.account.last_opened_lesson = None

    def _update_email(self, instance, email):
        EmailAddress.objects.add_email(user=instance, email=email)
        # Todo: add email changed specific response

    def _update_avatar(self, instance, request):
        avatar = Avatar(user=instance, primary=True)
        image_file = request.FILES['avatar']
        avatar.avatar.save(image_file.name, image_file)
        avatar.save()
        avatar_updated.send(sender=Avatar, user=instance, avatar=avatar)

    def update(self, instance, validated_data):
        request = self.context.get('request')
        account = validated_data.get('account', None)
        email = validated_data.get('email', None)

        # Update user
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)

        # Update account
        if account:
            self._update_account(instance, account)
            instance.account.save()

        # Update email
        if email and email != instance.email:
            self._update_email(instance, email)

        # Update avatar
        if 'avatar' in request.FILES:
            self._update_avatar(instance, request)

        instance.save()
        user_updated.send(sender=User, user=instance)
        return instance


class PasswordResetSerializer(serializers.Serializer):

    email = serializers.EmailField()

    def validate_email(self, email):
        if not EmailAddress.objects.filter(email=email).exists():
            raise serializers.ValidationError(_("The e-mail address is not assigned to any user account"))
        return email

    def save(self, *args, **kwargs):
        email = self.validated_data['email']
        user = EmailAddress.objects.get(email__iexact=email).user

        token = password_reset_token_generator.make_token(user)
        uid = int_to_base36(user.pk)

        send_password_reset_mail(user, token, uid)

        return email


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)
    uid = serializers.CharField()
    key = serializers.CharField()

    def validate_new_password1(self, password):
        validate_password(password)
        return password

    def validate(self, data):
        uid = data['uid']
        key = data['key']

        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError(_('The two password fields did not match.'))

        try:
            pk = base36_to_int(uid)
            self.user = User.objects.get(pk=pk)
            if not password_reset_token_generator.check_token(self.user, key):
                raise serializers.ValidationError(_('bad token'))

            return data
        except EmailAddress.DoesNotExist:
            raise serializers.ValidationError(_('bad token'))

    def save(self):
        password = self.validated_data['new_password1']
        self.user.set_password(password)
        self.user.save()


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128)
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)

    set_password_form_class = SetPasswordForm

    def __init__(self, *args, **kwargs):
        super(PasswordChangeSerializer, self).__init__(*args, **kwargs)

        self.request = self.context.get('request')
        self.user = getattr(self.request, 'user', None)

    def validate_old_password(self, password):
        if self.user and not self.user.check_password(password):
            raise serializers.ValidationError('Invalid password')
        return password

    def validate_new_password1(self, password):
        validate_password(password)
        return password

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError(_('The two password fields did not match.'))
        return data

    def save(self):
        password = self.validated_data['new_password1']
        self.user.set_password(password)
        self.user.save()
        update_session_auth_hash(self.request, self.user)


class TokenSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer()

    class Meta:
        model = Token
        fields = ('key', 'user')


# ------------------------------------- Registration --------------------------------------------------

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=30,
        min_length=3,
        required=True,
        error_messages={"min_length": _("تأكد أن اسم المستخدم يحتوي على 3 حروف على الأقل.")}
    )
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    name = serializers.CharField(
        max_length=100,
        min_length=5,
        required=True,
        error_messages={"min_length": _("تأكد أن تدخل اسمك الكامل (الاسم واللقب) وأنه لا يحتوي إلا على الحروف و المسافات, سيستعمل اسمك في إنتاج شهادتك.")}
    )

    def validate_name(self, name):
        pattern = '^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ðء-ي]+ [a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ðء-ي]+[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ðء-ي ]*$'
        compiler = re.compile(pattern)
        if not compiler.match(name):
            raise serializers.ValidationError(
                _("تأكد أن تدخل اسمك الكامل (الاسم واللقب) وأنه لا يحتوي إلا على الحروف و المسافات, سيستعمل اسمك في إنتاج شهادتك."))

        return name

    def validate_username(self, username):
        UnicodeUsernameValidator(username)
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                _("A user is already registered with this e-mail address."))
        return username

    def validate_email(self, email):
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError(
                _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        validate_password(password)
        return password

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('name', '')
        }

    def save(self):
        cd = self.get_cleaned_data()
        user = User.objects.create_user(cd['username'], cd['email'],
                                        cd['password1'], first_name=cd['first_name'])
        user.email_addresses.get(primary=True).send_confirmation()
        return user


class VerifyEmailSerializer(serializers.Serializer):
    uid = serializers.CharField(required=True)
    key = serializers.CharField(required=True)

    def validate(self, data):
        uid = data['uid']
        key = data['key']

        try:
            pk = base36_to_int(uid)
            self.email = EmailAddress.objects.get(pk=pk)
            if not confirm_email_token_generator.check_token(self.email, key):
                raise serializers.ValidationError(_('bad token'))
            return data
        except EmailAddress.DoesNotExist:
            raise serializers.ValidationError(_('bad token'))

    def save(self):
        is_changed = self.email.confirm()
        return self.email.email, is_changed


class ResendConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if not EmailAddress.objects.filter(email=email).exists():
            raise serializers.ValidationError(_("The e-mail address is not assigned to any user account"))
        return email

    def save(self):
        email = self.validated_data.get('email', '')
        EmailAddress.objects.get(email=email).send_confirmation()
