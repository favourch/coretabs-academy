
import os

# Base Settings
from .base import *

# Authentication and Avatars
from .account import *

# Logging
from .logging import *

if os.environ.get('HOST_ENV') == 'production':
    from .deploy_settings import *

LOGIN_URL = SPA_BASE_URL + '/signin'
