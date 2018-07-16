import os
import requests

from allauth.account.views import PasswordResetFromKeyView as PRV
from allauth.account.utils import perform_login

from rest_auth.views import LogoutView as LV
from rest_auth.registration.views import VerifyEmailView as VEV
from rest_auth.models import TokenModel
from rest_auth.app_settings import create_token

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView

from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout as django_logout
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from .serializers import ResendConfirmSerializer, UserDetailsSerializer, TokenSerializer

from .utils import sync_sso


class PasswordResetFromKeyView(PRV):
    success_url = reverse_lazy('home')


password_reset_from_key = PasswordResetFromKeyView.as_view()


class LogoutView(LV):
    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        if request.user.id:
            self.discourse_logout(request)

        django_logout(request)

        return Response({'detail': _('Successfully logged out.')},
                        status=status.HTTP_200_OK)

    def discourse_logout(self, request):
        data = {'api_key': settings.DISCOURSE_API_KEY,
                'api_username': settings.DISCOURSE_API_USERNAME}

        user = requests.get(settings.DISCOURSE_BASE_URL +
                            f'/users/by-external/{request.user.id}.json', data=data)

        user = user.json()
        user_id = user['user']['id']

        url = settings.DISCOURSE_BASE_URL + f'/admin/users/{user_id}/log_out/'

        r = requests.post(url, data=data)


logout_view = LogoutView.as_view()


class UserDetailsView(RetrieveUpdateAPIView):

    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


user_details_view = UserDetailsView.as_view()


class ResendConfirmView(GenericAPIView):

    serializer_class = ResendConfirmSerializer

    def post(self, request, *args, **kwargs):
        # Create a serializer with request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        # Return the success message with OK HTTP status
        return Response(
            {'detail': _('Confirmation e-mail has been sent.')},
            status=status.HTTP_200_OK
        )


resend_confirmation_view = ResendConfirmView.as_view()


class VerifyEmailView(VEV):
    token_model = TokenModel

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        self.serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = self.serializer.validated_data['key']
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        self.login_on_confirm(confirmation)
        return self.get_response()

    def login_on_confirm(self, confirmation):
        self.user = confirmation.email_address.user
        if self.user and self.request.user.is_anonymous:
            return perform_login(self.request,
                                 self.user,
                                 'none')

    def get_response(self):
        token = create_token(self.token_model, self.user, self.serializer)
        serializer_class = TokenSerializer

        serializer = serializer_class(instance=token,
                                      context={'request': self.request})

        return Response(serializer.data, status=status.HTTP_200_OK)


verify_email = VerifyEmailView.as_view()
