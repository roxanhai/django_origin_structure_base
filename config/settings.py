"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import datetime
import os
from pathlib import Path
from decouple import Config, RepositoryEnv, config
from core.my_settings import REST_FRAMEWORK, JWT_AUTH, SECRET_KEY, AUTH_USER_MODEL, SWAGGER_SETTINGS, \
    AUTHENTICATION_BACKENDS, SITE_ID, LOGIN_REDIRECT_URL, SOCIALACCOUNT_QUERY_EMAIL, ACCOUNT_LOGOUT_ON_GET, \
    ACCOUNT_EMAIL_REQUIRED, ACCOUNT_UNIQUE_EMAIL, SOCIALACCOUNT_PROVIDERS

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SERVER_ENV = os.environ.get('SERVER_ENV', 'dev')
env_config = config
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    #Additional
    'django.contrib.sites',
    'drf_yasg',
    "apps",
    "apps.users",
    "apps.authentication",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google'
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

ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# DATABASE SETTINGS
if env_config('DATABASES_NAME', 'None').lower() == 'postgres':
    DATABASES = {
        "default": {
            "ENGINE": env_config("POSTGRES_ENGINE", "django.db.backends.sqlite3"),
            "NAME": env_config("POSTGRES_DB", os.path.join(BASE_DIR, "db.sqlite3")),
            "USER": env_config("POSTGRES_USER", "admin"),
            "PASSWORD": env_config("POSTGRES_PASSWORD", "admin"),
            "HOST": env_config("POSTGRES_HOST", "localhost"),
            "PORT": env_config("POSTGRES_PORT", "5432"),
        }
    }
elif env_config('DATABASES_NAME', 'None').lower() == 'mysql':
    DATABASES = {
        'default': {
            'ENGINE': env_config("MY_SQL_ENGINE", "django.db.backends.sqlite3"),
            'NAME': env_config("MYSQL_DATABASE", "db"),
            'USER': env_config("MYSQL_USER", "admin"),
            'PASSWORD': env_config("MYSQL_PASSWORD", "admin"),
            'HOST': env_config("MY_SQL_HOST", "127.0.0.1"),
            'PORT': env_config("MYSQL_PORT", "3306"),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#CUSTOM SETTINGG
SECRET_KEY
REST_FRAMEWORK
JWT_AUTH
AUTH_USER_MODEL
SWAGGER_SETTINGS
AUTHENTICATION_BACKENDS

SITE_ID
LOGIN_REDIRECT_URL
SOCIALACCOUNT_QUERY_EMAIL
ACCOUNT_LOGOUT_ON_GET
ACCOUNT_UNIQUE_EMAIL
ACCOUNT_EMAIL_REQUIRED
SOCIALACCOUNT_PROVIDERS