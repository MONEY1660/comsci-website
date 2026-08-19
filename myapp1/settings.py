import os
from pathlib import Path
from urllib.parse import parse_qs, urlparse

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# Environment
# =========================================================

def load_environment_variables():
    env_file = BASE_DIR / ".env"

    if not env_file.exists():
        return

    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)

        key = key.strip()
        value = value.strip().strip("'\"")

        if key:
            os.environ.setdefault(key, value)


load_environment_variables()


# =========================================================
# Security
# =========================================================

SECRET_KEY = (
    os.environ.get("DJANGO_SECRET_KEY")
    or "django-insecure-development-key-change-this-in-production"
)

DEBUG = os.environ.get(
    "DJANGO_DEBUG",
    "False"
).lower() in ("1", "true", "yes", "on")


def get_allowed_hosts():

    raw_hosts = os.environ.get("ALLOWED_HOSTS", "")

    if raw_hosts:
        hosts = [
            host.strip()
            for host in raw_hosts.split(",")
            if host.strip()
        ]
    else:
        hosts = [
            "localhost",
            "127.0.0.1",
            ".vercel.app",
        ]

    vercel_url = os.environ.get("VERCEL_URL")

    if vercel_url:
        vercel_host = (
            vercel_url
            .replace("https://", "")
            .replace("http://", "")
            .split("/")[0]
        )

        if vercel_host not in hosts:
            hosts.append(vercel_host)

    return hosts


ALLOWED_HOSTS = get_allowed_hosts()


CSRF_TRUSTED_ORIGINS = [
    "https://*.vercel.app",
]

for host in ALLOWED_HOSTS:

    if host in ("localhost", "127.0.0.1"):

        CSRF_TRUSTED_ORIGINS.append(
            f"http://{host}"
        )

        CSRF_TRUSTED_ORIGINS.append(
            f"https://{host}"
        )

    elif host.startswith("."):

        CSRF_TRUSTED_ORIGINS.append(
            f"https://*{host}"
        )

    else:

        CSRF_TRUSTED_ORIGINS.append(
            f"https://{host}"
        )


SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)

USE_X_FORWARDED_HOST = True


# =========================================================
# Applications
# =========================================================

INSTALLED_APPS = [

    "django.contrib.admin",

    "django.contrib.auth",

    "django.contrib.contenttypes",

    "django.contrib.sessions",

    "django.contrib.messages",

    "django.contrib.staticfiles",

    "app1",
]


# =========================================================
# Middleware
# =========================================================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "myapp1.urls"


# =========================================================
# Templates
# =========================================================

TEMPLATES = [

    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],
        },
    },
]


WSGI_APPLICATION = "myapp1.wsgi.application"


# =========================================================
# DATABASE
# =========================================================

DATABASE_URL = os.environ.get("DATABASE_URL")


if DATABASE_URL:

    parsed_db = urlparse(DATABASE_URL)

    query_params = parse_qs(parsed_db.query)

    sslmode = query_params.get(
        "sslmode",
        ["require"]
    )[0]


    DATABASES = {

        "default": {

            "ENGINE": "django.db.backends.postgresql",

            "NAME": parsed_db.path.lstrip("/"),

            "USER": parsed_db.username,

            "PASSWORD": parsed_db.password,

            "HOST": parsed_db.hostname,

            "PORT": parsed_db.port or 5432,

            "OPTIONS": {

                "sslmode": sslmode,

            },
        }
    }

else:

    # Local development fallback

    DATABASES = {

        "default": {

            "ENGINE": "django.db.backends.sqlite3",

            "NAME": BASE_DIR / "db.sqlite3",

        }
    }


# =========================================================
# Password validation
# =========================================================

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",
    },

]


# =========================================================
# Internationalization
# =========================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Bangkok"

USE_I18N = True

USE_TZ = True


# =========================================================
# Static files
# =========================================================

STATIC_URL = "/static/"

STATICFILES_DIRS = [

    BASE_DIR / "statics",

    BASE_DIR / "static",

]

STATIC_ROOT = BASE_DIR / "staticfiles"


# =========================================================
# Media files
# =========================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# =========================================================
# Storage
# =========================================================

STORAGES = {

    "default": {

        "BACKEND":
        "django.core.files.storage.FileSystemStorage",

    },

    "staticfiles": {

        "BACKEND":
        "whitenoise.storage.CompressedStaticFilesStorage",

    },

}