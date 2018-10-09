import os

is_production = os.environ.get('HOST_ENV') == 'production'

if is_production:
    from .prod import *
else:
    from .dev import *

if True:
    try:
        from .dev_secrets import *
    except ModuleNotFoundError:
        pass
