"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 2.0.
For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from decouple import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
# from ecommerce.aws.conf import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

env = environ.Env()
env.read_env(env.str('ENV', '.env.local'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# VERSION
VERSION = config('VERSION')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['metalroofingonline.com.au', 'www.metalroofingonline.com.au', '103.11.147.91'] # , 'macbook1.local', '0.0.0.0', '127.0.0.1', 'mro-ecommerce.herokuapp.com'

MAILER_LIST = ['ryanjohndunne@gmail.com']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
BASE_URL = 'https://www.metalroofingonline.com.au'

MANAGERS = (
    ('Ryan Dunne', "metalroofingonlinemail@gmail.com")
)
ADMINS = (
    ('Ryan', 'ryanjohndunne@gmail.com'),
)



# Application definition

INSTALLED_APPS = [
    # Third party
    'storages',
    'bootstrap4',
    'bootstrap_datepicker_plus',
    'django_extensions',
    'jet.dashboard',
    'jet',
    'tinymce',
    'filebrowser',
    'simple_history',
    'adminsortable2',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.humanize',

    # Additional Apps Added
    'accounts',
    'addresses',
    'analytics',
    'billing',
    'categories',
    'carts',
    'header_message',
    'home_page',
    'footer_content',
    'images',
    'marketing',
    'orders',
    'products',
    'shipping',
    'search',
    'tags',
]

# Django contrib sites
SITE_ID = 1

# Change built-in user model to our custom model
AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = '/login/'
LOGIN_URL_REDIRECT = '/'
LOGOUT_URL = '/logout/'

FORCE_SESSION_TO_ONE = False
FORCE_INACTIVE_USER_ENDSESSION = False

MAILCHIMP_API_KEY = config('MAILCHIMP_API_KEY')
MAILCHIMP_DATA_CENTER = config('MAILCHIMP_DATA_CENTER')
MAILCHIMP_EMAIL_LIST_ID = config('MAILCHIMP_EMAIL_LIST_ID')

GOOGLE_API_KEY = config('GOOGLE_API_KEY')

STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY', cast=str)
STRIPE_PUB_KEY = config('STRIPE_PUB_KEY', cast=str)
#STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY', cast=str)
#STRIPE_PUB_KEY = config('STRIPE_TEST_PUB_KEY', cast=str)

XERO_CONSUMER_KEY = config('XERO_CONSUMER_KEY')
XERO_SECRET_KEY = config('XERO_SECRET_KEY')
XERO_RSA_KEY = config('RSA_KEY_PATH')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

LOGOUT_REDIRECT_URL = '/login/'
ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

            'libraries':{
                'custom_tags': 'templatetags.custom_tags',
            }
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'mro',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Melbourne'
DATE_FORMAT = ['%d-%m-%Y', '%d/%m/%Y']

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_my_proj"),
]
STATIC_ROOT = os.path.join(os.path.dirname(
    BASE_DIR), "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(
    BASE_DIR), "media")

# Filebrowser to choose image in tinymce
FILEBROWSER_DIRECTORY = ''
DIRECTORY = ''

# Doesn't Encrypt ssl/tls https for testing purposes
CORS_REPLACE_HTTPS_REFERER = False
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = None
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_FRAME_DENY = False
PREPEND_WWW = True

# Django-paypal settings
PAYPAL_RECEIVER_EMAIL = config('PAYPAL_RECEIVER_EMAIL')
PAYPAL_TEST = True

# Dashboard related
JET_INDEX_DASHBOARD = 'ecommerce.dashboard.CustomIndexDashboard'
JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

# # TinyMCE Related
TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 1120,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect, formatselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    }

# Include bootstrap4 jquery for datepicker
BOOTSTRAP4 = {
    'include_jquery': True,
}
