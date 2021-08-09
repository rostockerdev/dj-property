from .base import *
from decouple import config

###########################################
#        SECRET CONFIGURATION             #
###########################################

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']

###########################################
#        DATABASE CONFIGURATION           #
###########################################

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config('DB_NAME'),
        "USER": config('DB_USER'),
        "PASSWORD": config('DB_PASSWORD'),
        "HOST": config('DB_HOST'),
        "PORT": config('DB_PORT'),
    }
}

###########################################
#          WSGI CONFIGURATION             #
###########################################
WSGI_APPLICATION = 'core.wsgi.application'

###########################################
#        SECURITY CONFIGURATION           #
###########################################
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = False