from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
