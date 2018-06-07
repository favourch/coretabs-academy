import os, requests

from allauth.account.views import PasswordResetFromKeyView as PRV
from django.urls import reverse_lazy

from .utils import sync_sso

from rest_auth.views import LogoutView as LV
from rest_auth.registration.views import VerifyEmailView as VEV
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout as django_logout
from django.utils.translation import ugettext_lazy as _

from .serializers import ResendConfirmSerializer, UserDetailsSerializer, TokenSerializer
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView

from allauth.account.utils import perform_login


class PasswordResetFromKeyView(PRV):
    success_url = reverse_lazy("home")


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

        return Response({"detail": _("Successfully logged out.")},
                        status=status.HTTP_200_OK)

    def discourse_logout(self, request):
        data = {"api_key": os.environ.get('DISCOURSE_API_KEY'),
                     "api_username": os.environ.get('DISCOURSE_API_USERNAME')}

        user = requests.get( os.environ.get('DISCOURSE_HOST') + '/users/by-external/{}.json'.format(request.user.id), data=data)

        user = user.json()
        user_id = user['user']['id']

        url = os.environ.get('DISCOURSE_HOST') + '/admin/users/{}/log_out/'.format(user_id)

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
            {"detail": _("Confirmation e-mail has been sent.")},
            status=status.HTTP_200_OK
        )


resend_confirmation_view = ResendConfirmView.as_view()


class VerifyEmailView(VEV):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        self.login_on_confirm(confirmation)
        return self.get_response()

    def login_on_confirm(self, confirmation):
        user = confirmation.email_address.user
        if user and self.request.user.is_anonymous:
            return perform_login(self.request,
                                 user,
                                 'none')

    def get_response(self):
        serializer_class = TokenSerializer

        serializer = serializer_class(instance=self.request.user.auth_token,
                                          context={'request': self.request})

        return Response(serializer.data, status=status.HTTP_200_OK)


verify_email = VerifyEmailView.as_view()