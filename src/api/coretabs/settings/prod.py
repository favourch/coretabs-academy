from .base import *
import dj_database_url
from urllib.parse import quote_plus


SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False


# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}


# Hosts
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(';')


# URLs
SPA_BASE_URL = os.environ.get('SPA_BASE_URL')
API_BASE_URL = os.environ.get('API_BASE_URL')
LOGIN_URL = SPA_BASE_URL + '/signin'


# Cors Settings
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = os.environ.get('CORS_ORIGIN_WHITELIST').split(';')
CORS_ALLOW_CREDENTIALS = True


# CSRF & Session Domains
# Sample env var: 'coretabs.net = .coretabs.net; 127.0.0.1 = 127.0.0.1'
COOKIE_DOMAINS = dict((host, target) for host, target in (a.split('=')
                                                          for a in os.environ.get('COOKIE_DOMAINS').split(';')))


DEFAULT_COOKIE_DOMAIN = '127.0.0.1'
SESSION_COOKIE_DOMAIN = DEFAULT_COOKIE_DOMAIN
CSRF_COOKIE_DOMAIN = DEFAULT_COOKIE_DOMAIN

# EMAIL config
EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

EMAILS_MANAGERS = os.environ.get('EMAILS_MANAGERS').split(';')

MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
MAILGUN_MEMBERS_LIST = os.environ.get('MAILGUN_MEMBERS_LIST')
MAILGUN_LIST_DOMAIN = os.environ.get('MAILGUN_LIST_DOMAIN')


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


# DRF settings
REST_FRAMEWORK.update({
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
})


# Celery
AWS_ACCESS_KEY_ID = quote_plus(os.environ.get('CELERY_AWS_ACCESS_KEY_ID'))
AWS_SECRET_ACCESS_KEY = quote_plus(os.environ.get('CELERY_AWS_SECRET_ACCESS_KEY'))
CELERY_BROKER_URL = "sqs://{}:{}@".format(
    AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)


# Media Settings
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware', ]

# set S3 as the place to store your files.

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.environ.get('S3_AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('S3_AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '')

# This will make sure that the file URL does not have unnecessary parameters like your access key.
AWS_QUERYSTRING_AUTH = False

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# static media settings

STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/'
STATICFILES_DIRS = [(
    os.path.join(BASE_DIR, 'static')
)]
STATIC_ROOT = 'static_root'
ADMIN_MEDIA_PREFIX = f'{STATIC_URL}admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DEFAULT_FILE_STORAGE = 'coretabs.storage_backends.MediaStorage'
