from .base import *


DEBUG = True
ALLOWED_HOSTS = ['*', ]


DATABASES = {
    "default": dj_database_url.parse(os.environ.get(config("DATABASE_URL")))
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')