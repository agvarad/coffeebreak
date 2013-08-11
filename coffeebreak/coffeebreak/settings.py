from djangoappengine.settings_base import *

import os

SECRET_KEY = 'pxs7la(71lftc912^lc&amp;6^%6k1ap&amp;77+o5(6l5b3hjpf&amp;c7gd$'

INSTALLED_APPS = (
    'djangoappengine',
    'djangotoolbox',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'admin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'middleware.MinifyHTMLMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

LOGIN_REDIRECT_URL = '/admin/config'

ADMIN_MEDIA_PREFIX = '/media/admin/'
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)
COMPRESS_HTML = True

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'yourgmail_id.gmail.com'
EMAIL_HOST_PASSWORD = 'gmail_password'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'yourgmail_id.gmail.com'
EMAIL_BACKEND = 'appengine_emailbackend.EmailBackend'

ROOT_URLCONF = 'urls'
