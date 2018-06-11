

RAVEN_CONFIG = {
    'dsn': 'https://f8c998003d4a47d1953c190ceb71a025:c4818e89d3b74807bb6f5047060d498a@sentry.io/1222620'
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['sentry'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}