import os


if os.environ.get('HOST_ENV') == 'production':
    from .prod import *
else:
    from .dev import *
