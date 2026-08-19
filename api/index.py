import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp1.settings")

# NOTE: staticfiles/ (STATIC_ROOT) is committed to the repo and served by
# WhiteNoiseMiddleware at runtime. Vercel's serverless filesystem is
# read-only outside of /tmp, so `collectstatic` cannot run here — it must
# be run locally (`python manage.py collectstatic`) any time files under
# static/ or statics/ change, with the output committed to git.

application = get_wsgi_application()
app = application
