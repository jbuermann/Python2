import os
import sys
import site

site.addsitedir('/var/www/html/bpEnv/local/lib/python2.7/site-packages')

sys.path.append('/var/www/html/theworst')
sys.path.append('/var/www/html/theworst/theworst')

os.environ['DJANGO_SETTINGS_MODULE'] = 'theworst.settings.production'

activate_env=os.path.expanduser("/var/www/html/bpEnv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()