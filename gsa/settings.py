from pathlib import Path
import os
from django.contrib.messages import constants as messages_constants
from decouple import config
from dj_database_url import parse as dburl

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['www.gsaportaria.com.br', 'gsaportaria.com.br', 'localhost', '127.0.0.1', '0.0.0.0', '172.16.1.9']
# ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',
    'rest_framework',
    'global_permissions',
    'django_filters',
    'tinymce',
    'captcha',

    'apps.servicos.templatetags',

    'apps.home',
    'apps.servicos',
    'apps.empresas',
    'apps.gerador_qrcode',
    'apps.users',
    'apps.apontamento',
    'apps.contato',
    'apps.blog',
    'apps.tag',
    'apps.orcamentos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware', )

ROOT_URLCONF = 'gsa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # apps
                'apps.home.context_processors.site_infor',
                'apps.home.context_processors.servicos_categorias',
            ],
        },
    },
]

WSGI_APPLICATION = 'gsa.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
if DEBUG:
    default_dburl = config('DEV_DATABASE_URL')
else:
    default_dburl = config('PROD_DATABASE_URL')
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

DATE_INPUT_FORMATS = '%d-%m-%Y'
TIME_INPUT_FORMATS = ['%H:%M:%S']

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = False

USE_L10N = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_URL = "/media/"
if not DEBUG:
    STATIC_ROOT = "/home/gsaporta/www/static"
    MEDIA_ROOT = "/home/gsaporta/www/media/"
else:
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    # MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# configuração de email

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_Host')
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_Host_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_Host_PASSWORD')
EMAIL_USE_SSL = False


AUTH_USER_MODEL = 'users.User'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'apps.users.backends.ModelBackend',
)
LOGIN_REDIRECT_URL = '/apontamento/registros/'


MESSAGE_TAGS = {
    messages_constants.DEBUG: 'debug',
    messages_constants.INFO: 'info',
    messages_constants.SUCCESS: 'success',
    messages_constants.WARNING: 'warning',
    messages_constants.ERROR: 'danger',
}

TINYMCE_DEFAULT_CONFIG = {
    "plugins": "advlist,autolink,lists,link,image,charmap,print,preview,anchor,searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,", #plugins
    "toolbar":"undo redo | formatselect | image |", #toolbar
    "height": 500, #texteditor height
}

RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']


RECAPTCHA_PROXY = {'http': 'http://127.0.0.1:8000', 'https': 'https://127.0.0.1:8000'}