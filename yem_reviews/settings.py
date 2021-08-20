from pathlib import Path
from django.conf.global_settings import AUTH_USER_MODEL, EMAIL_BACKEND, STATICFILES_DIRS
import os
import environ

env = environ.Env(
    DEBUG=(bool, False)
)

# READ_DOT_ENV_FILE = env.bool('READ_DOT_ENV_FILE', default=False)
# if READ_DOT_ENV_FILE:
#     environ.Env.read_env()

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')


BASE_DIR = Path(__file__).resolve().parent.parent


ALLOWED_HOSTS = [
    'yemreviews.herokuapp.com',
    'localhost',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    

    #Third party apps
    'crispy_forms',
    'crispy_tailwind',

    #Local apps
    'movies',

    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'yem_reviews.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / "templates" ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'yem_reviews.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         ''
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'yem_reviews',
        'USER': 'yemi',
        'PASSWORD': 'lanre',
        'HOST': 'localhost',
        'PORT': '',
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/



LOGIN_REDIRECT_URL = "/"
USE_S3 = os.getenv('USE_S3') or False

# Mba use the function commented above instead of just setting it to True as I did
# USE_S3 = True

if USE_S3:
    
    # You will have to configure everything below here under your environment variables
    # and don't forget to delete your public repo or make it privare 

    # aws settings
    AWS_ACCESS_KEY_ID="AKIAWYKSAQU5HQGB2VFZ"

    AWS_SECRET_ACCESS_KEY="bXB22/xQcUw70cPcdda8fLSrE8G0aJME5/ixAVrb"

    AWS_STORAGE_BUCKET_NAME="movie-review-files"
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_S3_FILE_OVERWRITE = False

    # s3 media settings
    PUBLIC_MEDIA_LOCATION = 'movie_posters'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'movies.storage_backends.PublicMediaStorage'


    # s3 static settings
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

else: 

    # STATIC_URL = '/static/'
    # STATIC_ROOT = "staticfiles"

    STATICFILES_DIRS = [BASE_DIR / "static"]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = 'https://movie-review-files.s3.us-west-2.amazonaws.com/'
MEDIA_URL = '/media/'


AUTH_USER_MODEL = "movies.User"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"



DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
