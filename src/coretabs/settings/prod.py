from .base import *
import dj_database_url


SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False


# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}


# Hosts
ALLOWED_HOSTS = [
    'www.coretabs.net',
    '.coretabs.net',
    '0.0.0.0'
]


# URLs
SPA_BASE_URL = os.environ.get('SPA_BASE_URL')
API_BASE_URL = os.environ.get('API_BASE_URL')
LOGIN_URL = SPA_BASE_URL + '/signin'


# Cors Settings
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'spa.coretabs.net', 'www.coretabs.net', 'coretabs.net')
CORS_ALLOW_CREDENTIALS = True


# CSRF and Session
SESSION_COOKIE_DOMAIN = '.coretabs.net'
CSRF_COOKIE_DOMAIN = '.coretabs.net'


# EMAIL config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

MANAGERS_EMAILS = os.environ.get('MANAGERS_EMAILS').split(';')


# Discourse Settings
DISCOURSE_BASE_URL = os.environ.get('DISCOURSE_BASE_URL')
DISCOURSE_SSO_SECRET = os.environ.get('DISCOURSE_SSO_SECRET')
DISCOURSE_API_KEY = os.environ.get('DISCOURSE_API_KEY')
DISCOURSE_API_USERNAME = os.environ.get('DISCOURSE_API_USERNAME')


# Cache Setup

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/tmp/memcached.sock',
    }
}

# Logging Settings
RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_DSN'),
}

DJANGO_LOGGING = {
    'SQL_LOG': False,
    'CONSOLE_LOG': False,
}


# Media Settings
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware', ]
