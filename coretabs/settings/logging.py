

RAVEN_CONFIG = {
    'dsn': 'https://f8c998003d4a47d1953c190ceb71a025:c4818e89d3b74807bb6f5047060d498a@sentry.io/1222620'
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'rest',
        },
        'sentry': {
            'level': 'INFO',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
    },
    'formatters': {
        'rest': {
            'format': '%(levelname)-8s %(asctime)s \n'
                      '   %(message)s'
        },
    },
    'loggers': {
        '': {
            'handlers': ['sentry'],
            'level': 'WARNING',
            'propagate': True,
        },
        'rest': {
            'level': 'INFO',
            'handlers': ['file'],
            # required to avoid double logging with root logger
            'propagate': False,
        },
    },
}