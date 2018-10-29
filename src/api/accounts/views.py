from django.contrib.auth import (
    login as django_login,
    logout as django_logout
)
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token

from .serializers import (
    TokenSerializer, UserDetailsSerializer, LoginSerializer,
    PasswordResetSerializer, PasswordResetConfirmSerializer,
    PasswordChangeSerializer, RegisterSerializer, VerifyEmailSerializer,
    ResendConfirmSerializer,
)
from .utils import create_token

from .tasks import discourse_logout

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'password', 'old_password', 'new_password1', 'new_password2'
    )
)


class LoginView(GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    response_serializer_class = TokenSerializer
    token_model = Token

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def get_response(self, request, token):
        serializer = self.response_serializer_class(instance=token, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        django_login(request, user)
        token = create_token(self.token_model, user)

        return self.get_response(request, token)


class LogoutView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        self.logout(request)

        # TODO: use locale instead
        return Response({'detail': _("تم تسجيل الخروج بنجاح")}, status=status.HTTP_200_OK)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        if request.user.id:
            discourse_logout.delay(request.user.id)

        django_logout(request)


class UserDetailsView(RetrieveUpdateAPIView):

    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class PasswordResetView(GenericAPIView):

    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": _("Password reset e-mail has been sent.")}, status=status.HTTP_200_OK)


class PasswordResetConfirmView(GenericAPIView):

    serializer_class = PasswordResetConfirmSerializer
    permission_classes = (AllowAny,)

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(PasswordResetConfirmView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": _("Password has been reset with the new password.")},
            status=status.HTTP_200_OK
        )


class PasswordChangeView(GenericAPIView):

    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(PasswordChangeView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": _("New password has been saved.")})


# ------------------------------------- Registration --------------------------------------------------

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny, ]
    token_model = Token

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        create_token(self.token_model, user)

        return Response({"detail": _("Verification e-mail sent.")},
                        status=status.HTTP_201_CREATED)


class VerifyEmailView(GenericAPIView):
    permission_classes = [AllowAny, ]
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')
    serializer_class = VerifyEmailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": _("Email Confirmed")}, status=status.HTTP_200_OK)


class ResendConfirmView(GenericAPIView):
    permission_classes = [AllowAny, ]
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')
    serializer_class = ResendConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'detail': _("Verification e-mail sent.")}, status=status.HTTP_200_OK)
