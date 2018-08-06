from .base import *


SECRET_KEY = '#g61i*t=xzc3ogr#&lajy6$si-db0=%9y8d@0_fs(5n*j%q@^p'
DEBUG = True


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Hosts
ALLOWED_HOSTS = ['192.168.99.100', 'localhost', '127.0.0.1']


# Only for DEBUG
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda x: True
}


# URLs
SPA_BASE_URL = 'https://spa.coretabs.net'
API_BASE_URL = '127.0.0.1:8000'
LOGIN_URL = SPA_BASE_URL + '/signin'


# CORS settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


# CSRF and Session
SESSION_COOKIE_DOMAIN = '127.0.0.1'
CSRF_COOKIE_DOMAIN = '127.0.0.1'


# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
MANAGERS_EMAILS = ['one@gmail.com', 'two@gmail.com']


# Logging settings
RAVEN_CONFIG = {
    'dsn': 'https://90efcbde7722405e90d6878c7e936a9d:7b26ebbf78194fe99f35cf508dfee166@sentry.io/1225004'
}

# Discourse Settings
DISCOURSE_BASE_URL = os.environ.get('DISCOURSE_BASE_URL')
DISCOURSE_SSO_SECRET = os.environ.get('DISCOURSE_SSO_SECRET')
DISCOURSE_API_KEY = os.environ.get('DISCOURSE_API_KEY')
DISCOURSE_API_USERNAME = os.environ.get('DISCOURSE_API_USERNAME')