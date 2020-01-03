from .base import *
import dj_database_url

os.environ['SECRET_KEY'] = '5n@_$tgyve8=(oo)no1ys8h%=mto!a!r1tq%-9!)&g-z6o9fso'
SECRET_KEY = os.environ['SECRET_KEY'] 
DEBUG = True #TODO: Turn off on realease

ALLOWED_HOSTS += ["demo.dabolinux.com",]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'uniondb',
        'USER': 'union',
        'PASSWORD': 'Pass@1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DATABASES_URL = os.environ['DATABASE_URL'] 
DATABASES['default'] = dj_database_url.parse(DATABASES_URL, conn_max_age=600)


STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/unionstatic/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
MEDIA_URL = '/unionmedia/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

HOST = "https://dabolinux.com"

# Google cloud for images
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_PROJECT_ID ='dabolinux'
GS_BUCKET_NAME = 'dabolinux_tech_clients'
GS_SERVICE_ACCOUNT = 'dabolinux-clients-demo@dabolinux.iam.gserviceaccount.com'
GS_FILE_OVERWRITE = True
GS_LOCATION = 'clients_demo'

from google.oauth2 import service_account
GS_AUTH_FILE = os.path.join(PROJECT_ROOT, "dabolinux-clients-demo-32103b022bf6.json")
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    GS_AUTH_FILE)