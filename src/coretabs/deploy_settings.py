from .settings import *
import dj_database_url


SPA_BASE_URL = os.environ.get(SPA_BASE_URL)

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = [
    'www.coretabs.net',
    'coretabs.net',
    '0.0.0.0'
]

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}


# EMAIL config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')

DISCOURSE_BASE_URL = os.environ.get('DISCOURSE_HOST')
DISCOURSE_SSO_SECRET = os.environ.get('DISCOURSE_SSO_SECRET')
DISCOURSE_API_KEY = os.environ.get('DISCOURSE_API_KEY')
DISCOURSE_API_USERNAME = os.environ.get('DISCOURSE_API_USERNAME')

if os.environ.get('ADMIN_EMAILS'):
    MANAGERS_EMAILS = os.environ.get('ADMIN_EMAILS').split(';')

RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_DSN'),
}

DJANGO_LOGGING = {
    "SQL_LOG": False,
    'CONSOLE_LOG': False,
}

MIDDLEWARE += [
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware']
