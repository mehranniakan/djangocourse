"""
Django settings for djangoProject project.

Generated by 'django-admin startproject' using Django 4.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3qn$aihh0$z)gw+s_)7t(t%*q9#&%+h-z*$96-q8qd#s_k=%jg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 2
# Application definition
ROBOTS_USE_SITEMAP = False

SUMMERNOTE_THEME = 'bs4'

X_FRAME_OPTIONS = "SAMEORIGIN"

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

ACCOUNT_SIGNUP_REDIRECT_URL = "/"

ACCOUNT_FORMS = {'signup': 'custom_account.forms.MyCustomSignupForm'}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mehran613.niakan@gmail.com'
EMAIL_HOST_PASSWORD = 'avgj ebbh dddl hpll'

INSTALLED_APPS = [
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django_extensions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'robots',
    "taggit",
    "captcha",
    "custom_account",
    'django_summernote',
    "debug_toolbar",
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'website.apps.WebsiteConfig',
    'allauth',
    'allauth.account',
    'compressor',
    "cssmin",
    "jsmin",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'djangoProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'Templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travel',
        'USER': 'KmcAuth',
        'PASSWORD': 'rkqONSGSGKA8)O(w',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]

# COMPRESS_ENABLED = True
# COMPRESS_ROOT = STATIC_ROOT ##django compressor
# COMPRESS_OFFLINE = True
#
# if not COMPRESS_ENABLED: ##django compressor
# COMPRESS_ENABLED = True
# COMPRESS_CSS_FILTERS = ["compressor.filters.cssmin.CSSMinFilter"]
# COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"] ##django compressor

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    "127.0.0.1",
]

MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}

LOGIN_REDIRECT_URL = '/'
