from .base import *

SECRET_KEY = 'django-insecure-em=+h!1nwy)dt_np^ztxh=iwmhzu$gyi=93(b8@-qnd6r00dn^'
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}