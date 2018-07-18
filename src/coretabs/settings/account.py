import os

# Account Settings
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_MIN_LENGTH = 3
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'
ACCOUNT_ADAPTER = 'hacks.adapter.MyAccountAdapter'
ACCOUNT_USERNAME_BLACKLIST = ['system', ]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

OLD_PASSWORD_FIELD_ENABLED = True

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'hacks.serializers.LoginSerializer',
    'USER_DETAILS_SERIALIZER': 'hacks.serializers.UserDetailsSerializer',
    'PASSWORD_RESET_SERIALIZER': 'hacks.serializers.PasswordResetSerializer',
    'PASSWORD_RESET_CONFIRM_SERIALIZER': 'hacks.serializers.PasswordResetConfirmSerializer',
    'TOKEN_SERIALIZER': 'hacks.serializers.TokenSerializer'
}

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'hacks.serializers.RegisterSerializer',
}

MANAGERS_EMAILS = ['one@gmail.com', 'two@gmail.com']

AVATAR_CLEANUP_DELETED = True
AVATAR_MAX_AVATARS_PER_USER = 1

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
