import os
from pathlib import Path
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp1.settings")

# Ensure staticfiles directory is generated if missing
base_dir = Path(__file__).resolve().parent.parent
staticfiles_dir = base_dir / "staticfiles"
if not staticfiles_dir.exists():
    try:
        import django
        from django.core.management import call_command
        django.setup()
        call_command("collectstatic", interactive=False)
    except Exception:
        pass

application = get_wsgi_application()
app = application
