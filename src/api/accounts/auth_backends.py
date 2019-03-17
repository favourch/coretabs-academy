from django.contrib.auth.backends import ModelBackend

from .models import EmailAddress
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthenticationBackend(ModelBackend):

    def authenticate(self, **credentials):
        ret = self._authenticate_by_email(**credentials)
        if not ret:
            ret = self._authenticate_by_username(**credentials)

        return ret

    def _authenticate_by_username(self, **credentials):
        username = credentials.get('username')
        password = credentials.get('password')

        if username is None:
            return None
        try:
            user = User._default_manager.get_by_natural_key(username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            User().set_password(password)
            return None

    def _authenticate_by_email(self, **credentials):
        email_address = credentials.get('email')
        password = credentials.get('password')

        if email_address is None:
            return None

        try:
            email = EmailAddress.objects.get(email__iexact=email_address, primary=True)
            user = email.user
            if user.check_password(password):
                return user
        except EmailAddress.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            User().set_password(password)
            return None
