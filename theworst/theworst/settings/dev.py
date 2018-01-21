from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jrj(e7*nk22818pt$fou7208%2!!^!vr($ve*qa)z0-=6)_^g!'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

try:
    from .local import *
except ImportError:
    pass
