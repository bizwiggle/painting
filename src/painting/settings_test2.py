"""
Django settings for bizwiggle project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from painting.constants import SITE_IDS
from painting.email_settings import *

SITE_NAME = 'test2.bizwiggle.com'
SITE_ID = SITE_IDS[SITE_NAME]

STRIPE_PLAN = 'painting9999'
TRIAL_LENGTH = 7

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't^4$*8)2e=1ls8@=jy=z(#!3thj##0uvj&5$5065*w31bao5jz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['.bizwiggle.com']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'imagekit',
    'auth',
    'pages',
    'interface',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Authorization
AUTH_USER_MODEL = 'auth.MyUser'
LOGIN_URL = '/admin/login/'

ROOT_URLCONF = 'painting.urls'

WSGI_APPLICATION = 'painting.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = ( 
    os.path.join(os.path.dirname(BASE_DIR), 'static', 'templates'),
)

MEDIA_URL = '/media/'

if DEBUG:
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static', 'static-only')  
else:
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static-only')  

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static', 'media') 
STATICFILES_DIRS = ( 
        os.path.join(os.path.dirname(BASE_DIR), 'static', 'static'), 
    )   