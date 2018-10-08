import os


if os.environ.get('HOST_ENV') == 'production':
    from .prod import *
else:
    from .dev import *

if True:
    try:
        from .dev_secrets import *
    except ModuleNotFoundError:
        pass
