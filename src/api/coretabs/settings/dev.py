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


# CSRF & Session Domains
COOKIE_DOMAINS = {
    'https://coretabs.net': '.coretabs.net',
    'http://127.0.0.1:8000': '127.0.0.1',
    'http://127.0.0.1:8080': '127.0.0.1',
    'http://localhost:8080': '127.0.0.1'
}


DEFAULT_COOKIE_DOMAIN = '127.0.0.1'
SESSION_COOKIE_DOMAIN = DEFAULT_COOKIE_DOMAIN
CSRF_COOKIE_DOMAIN = DEFAULT_COOKIE_DOMAIN

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# run "python -m smtpd -n -c DebuggingServer localhost:1025"
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAILS_MANAGERS = ['one@gmail.com', 'two@gmail.com']
MAILGUN_LIST_DOMAIN = 'api.coretabs.net'


# Logging settings
RAVEN_CONFIG = {
    'dsn': 'https://90efcbde7722405e90d6878c7e936a9d:7b26ebbf78194fe99f35cf508dfee166@sentry.io/1225004'
}

# Discourse Settings
# Mock server
DISCOURSE_BASE_URL = 'https://dc0e4c02-28ca-4dc7-8da9-cb7f696ea077.mock.pstmn.io'
DISCOURSE_API_KEY = 'anilliqnmsakmcnahojdwklaklsa'
DISCOURSE_API_USERNAME = 'discourse_mock'
DISCOURSE_SSO_SECRET = 'd836444a9e4084d5b224a60c208dce14'


# Celery
CELERY_BROKER_URL = "amqp://guest:guest@127.0.0.1:5672//"
