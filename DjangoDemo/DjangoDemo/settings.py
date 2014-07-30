"""
Django settings for DjangoDemo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from sqlalchemy import create_engine
import logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&tlpsas=c^pkzyie-)#m5or$+1b_-pen(i4*m=aieb#al)ogw-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DemoMain',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'DjangoDemo.urls'

WSGI_APPLICATION = 'DjangoDemo.wsgi.application'

HERE = os.path.dirname(__file__)
WEPAY_DB_PATH = os.path.abspath(os.path.join(HERE, '../../database/db.db3'))
LOG_PATH = os.path.abspath(os.path.join(HERE, '../../log/demo.log'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.abspath(os.path.join(HERE, '../../database/db_User.sqlite3')),
    }
}

DBN = r'sqlite:///%s' % WEPAY_DB_PATH
#DBN = r'mysql://wepay:wepay@203.195.184.208/wepay?charset=utf8'
engine = create_engine(DBN, echo=False, pool_recycle=7200)
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

RESOURCE_PATH = os.path.abspath(os.path.join(HERE, '../../resources'))

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] [%(filename)s]: %(levelname)s - %(message)s',
                    #datefmt='%a, %d %b %Y %H:%M:%S',
                    datefmt='%Y-%m-%d %X',
                    filename=LOG_PATH,
                    filemode='a')