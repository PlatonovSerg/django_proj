"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    "django-insecure-9ea(zz+#z&^o6)*+-7$=qm-$$yd-y1=dvaygj+a9h$7_p-3j-*"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "*",
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    "51.250.32.232",
    "http://51.250.32.232",
    "::1",
    "platonov1727.ru",
    "platonov1727.ru/blog"
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog.apps.BlogConfig",
    "taggit",
    # "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.postgres",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
if DEBUG is True:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "/data/db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            # Меняем настройку Django: теперь для работы будет использоваться
            # бэкенд postgresql
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRES_DB", "blog"),
            "USER": os.getenv("POSTGRES_USER", "blog"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD", ""),
            "HOST": os.getenv("DB_HOST", ""),
            "PORT": os.getenv("DB_PORT", "5432"),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Email settings SMTP


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = (os.getenv("EMAIL_HOST", ""),)
EMAIL_PORT = (os.getenv("EMAIL_PORT", ""),)
EMAIL_USE_TLS = (os.getenv("EMAIL_USE_TLS", ""),)
EMAIL_USE_SSL = (os.getenv("EMAIL_USE_SSL", ""),)
EMAIL_HOST_USER = (os.getenv("EMAIL_HOST_USER", ""),)
EMAIL_HOST_PASSWORD = (os.getenv("EMAIL_HOST_PASSWORD", ""),)


CSRF_TRUSTED_ORIGINS = [
    "http://51.250.32.232",
    "platonov1727.ru",
    "http://51.250.32.232/admin/",
    "http://51.250.32.232/blog/",
    "http://platonov1727.ru",
    "https://platonov1727.ru",
    "http://platonov1727.ru/admin",
    "http://platonov1727.ru/blog",
    "https://platonov1727.ru/admin/",
    "https://platonov1727.ru/blog/",
    "https://platonov1727.ru/blog/",
    "localhost:8000",
    "localhost",
    "http://localhost:8000",
    "http://localhost",
]
