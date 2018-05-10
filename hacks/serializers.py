import re
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from .utils import sync_sso

from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer as RS
from rest_auth.serializers import PasswordResetSerializer as PRS
from allauth.account.forms import ResetPasswordForm

from allauth.account.utils import send_email_confirmation
from library.serializers import ProfileSerializer

UserModel = get_user_model()


class RegisterSerializer(RS):
    name = serializers.CharField(
        max_length=100,
        min_length=5,
        required=True
    )

    def validate_name(self, name):
        pattern = "^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ðء-ي]+ [a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ðء-ي]+[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ðء-ي ]*$"
        compiler = re.compile(pattern)
        if not compiler.match(name):
            raise serializers.ValidationError(
                _("Make sure that you passed your fullname and that it contains only letters."))

        return name

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('name', '')
        }

    def custom_signup(self, request, user):
        sync_sso(user)


class PasswordResetSerializer(PRS):
    password_reset_form_class = ResetPasswordForm

    def save(self):
        request = self.context.get('request')
        self.reset_form.save(request)

    def validate_email(self, email):
        return email

    def validate(self, attrs):
        # Create PasswordResetForm with the serializer
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)

        return attrs


class ResendConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()

    password_reset_form_class = ResetPasswordForm

    def validate(self, attrs):
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)

        return attrs

    def save(self):
        request = self.context.get('request')
        User = get_user_model()
        email = self.reset_form.cleaned_data["email"]
        user = User.objects.get(email=email)
        send_email_confirmation(request, user, True)
        return email


class UserDetailsSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    name = serializers.CharField(source='first_name',
                                 max_length=100,
                                 min_length=5,
                                 required=True)

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'name', 'profile')
        read_only_fields = ('email', )

    def validate_name(self, name):
        pattern = "^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ðء-ي]+ [a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ðء-ي]+[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ðء-ي ]*$"
        compiler = re.compile(pattern)
        if not compiler.match(name):
            raise serializers.ValidationError(
                _("Make sure that you passed your fullname and that it contains only letters."))

        return name

    def update(self, instance, validated_data):
        profile = validated_data.pop('profile')
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.profile.track = profile.get('track', instance.profile.track)
        instance.profile.last_opened_lesson = profile.get('last_opened_lesson', instance.profile.last_opened_lesson)
        instance.save()
        return instance
