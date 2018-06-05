from coretabs.settings import *
import dj_database_url


SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
    'www.coretabs.net',
    'coretabs.net',
    '192.168.99.100',
    '172.17.0.1',
    '0.0.0.0'
]

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}


MIDDLEWARE += [
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware']
