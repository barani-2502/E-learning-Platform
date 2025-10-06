from .base import *

DEBUG = False

ADMINS = (
    ('Barani B', 'barani2502@gmail.com')
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'admin123',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}