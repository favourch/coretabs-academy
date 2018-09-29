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
ALLOWED_HOSTS = [
    'www.coretabs.net',
    '.coretabs.net',
    '0.0.0.0',
    '.compute.amazonaws.com',
    '.elasticbeanstalk.com' 
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
EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
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


# DRF settings
REST_FRAMEWORK.update({
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
})


# Celery
AWS_ACCESS_KEY_ID = quote_plus(os.environ.get('AWS_ACCESS_KEY_ID'))
AWS_SECRET_ACCESS_KEY = quote_plus(os.environ.get('AWS_SECRET_ACCESS_KEY'))
CELERY_BROKER_URL = "sqs://{}:{}@".format(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)


# Media Settings
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware', ]

# set S3 as the place to store your files.

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.environ.get('S3_AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('S3_AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '')

AWS_QUERYSTRING_AUTH = False # This will make sure that the file URL does not have unnecessary parameters like your access key.

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

#static media settings

STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'
MEDIA_URL = STATIC_URL + 'media/'
STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = 'static_root'
ADMIN_MEDIA_PREFIX = f'{STATIC_URL}admin/'

STATICFILES_FINDERS = (
'django.contrib.staticfiles.finders.FileSystemFinder',
'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
