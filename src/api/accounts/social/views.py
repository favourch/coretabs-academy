from django.contrib.auth import login as django_login

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from .serializers import SocialSerializer
from ..serializers import TokenSerializer

from .utils import get_social_auth, get_user_by_email, create_user_social, create_social_auth


class SocialLoginView(GenericAPIView):

    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')
    serializer_class = SocialSerializer
    response_serializer_class = TokenSerializer

    def get_response(self, request, token):
        serializer = self.response_serializer_class(instance=token, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        backend, access_token = serializer.get_data()
        social_data = backend.get_clean_data(access_token)
        social_auth = get_social_auth(social_data['uid'], backend.name)

        if social_auth is None:
            user = get_user_by_email(social_data['email'])

            if user is None:
                user = create_user_social(social_data)

            social_auth = create_social_auth(user, social_data['uid'], backend.name)

        else:
            user = social_auth.user

        if user:
            user.backend = backend.name
            django_login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return self.get_response(request, token)

        return Response(status=status.HTTP_400_BAD_REQUEST)
