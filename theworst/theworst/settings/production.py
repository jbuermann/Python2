from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

SERVER_EMAIL = 'jordan.buermann@gmail.com'
ADMINS = [('Jordan', 'jordan.buermann@gmail.com')]

ALLOWED_HOSTS = ['www.bpevents.org','bpevents.org']

with open('/home/buermann/bpevents/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # Log to a text file that can be rotated by logrotate
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/apache2/buermann-theworst-error.log'
        },
    },
    'loggers': {
        # Again, default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'myapp': {
            'handlers': ['logfile'],
            'level': 'WARNING', # Or maybe INFO or DEBUG
            'propagate': False
        },
    },
}

try:
    from .local import *
except ImportError:
    pass
