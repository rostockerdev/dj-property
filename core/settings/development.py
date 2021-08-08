from .base import *
from decouple import config

###########################################
#        SECRET CONFIGURATION             #
###########################################
SECRET_KEY = config('SECRET_KEY')
# DEBUG = config('DEBUG', default=False, cast=bool)
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

###########################################
#        DATABASE CONFIGURATION           #
###########################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

###########################################
#          WSGI CONFIGURATION             #
###########################################
WSGI_APPLICATION = 'core.wsgi.application'
