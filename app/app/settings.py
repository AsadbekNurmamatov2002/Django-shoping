import os, mimetypes
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "changememyprojects1")
# DEBUG = bool(int(os.environ.get('DEBUG', 0)))
DEBUG=True
ALLOWED_HOSTS = []
# ALLOWED_HOSTS.extend(
#     filter(
#         None,
#         os.environ.get('ALLOWED_HOSTS', '').split(','),
#     )
# )


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'product.apps.ProductConfig',
    'orders.apps.OrdersConfig',
    'cart.apps.CartConfig',
    'category.apps.CategoryConfig',
    'users.apps.UsersConfig',

    'django_recaptcha',

    'debug_toolbar',

]


REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
# chache 
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(BASE_DIR.parent, 'cache'),
    }
}

INTERNAL_IPS = [
 '127.0.0.1',
] 
if DEBUG:
   mimetypes.add_type('application/javascript', '.js', True)
   mimetypes.add_type('text/css', '.css', True)

AUTH_USER_MODEL='users.User'
CART_SESSION_ID='cart'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
                'category.context_processors.CategoryA',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'
# capcha
RECAPTCHA_PUBLIC_KEY = '6LecRYUpAAAAALwA8kzSTP1cD9WkGTMTZJiH9lcF'
RECAPTCHA_PRIVATE_KEY = '6LecRYUpAAAAADIdHIm8MsromeHjhj3gw84qfO5Q'
# RECAPTCHA_PROXY = {'http': 'http://127.0.0.1:8000', 'https': 'https://127.0.0.1:8000'}
# RECAPTCHA_DOMAIN = 'www.recaptcha.net'
# user

# AUTHENTICATION_BACKENDS = [
#  'django.contrib.auth.backends.ModelBackend',
#  'account.authentication.EmailAuthBackend',
# ]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': os.environ.get('DB_HOST'),
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASS'),
#     }
# }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_FROM = 'nurmamatovasadbek85@gmail.com'
EMAIL_HOST_USER = 'pythonlessons0@gmail.com'
EMAIL_HOST_PASSWORD = 'urjp mdjw tqwo kumt'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

PASSWORD_RESET_TIMEOUT = 14400


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL='media/'
STATIC_ROOT=os.path.join(BASE_DIR.parent, 'staticfile')
MEDIA_ROOT=os.path.join(BASE_DIR.parent, 'media')
STATICFILES_DIRS=[
    os.path.join(BASE_DIR.parent, 'static')
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
