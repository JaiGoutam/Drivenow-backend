from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-je=4n*c*24!!fcdc-9306(!co&4ntp)_7w9f((ri307&r(#xss'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'dev_jai.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dev_jai.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "aws-1-ap-south-1.pooler.supabase.com",
        "PORT": "5432",
        "NAME": "postgres",
        "USER": "postgres.bwpuiqeqtotgcmgbzoww",
        "PASSWORD": "Jaishika@2212",
    }
}



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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'






ALLOWED_HOSTS = ["*"]

# AUTH_USER_MODEL = "back.SystemUser"

CORS_ORIGIN_ALLOW_ALL = True

APPEND_SLASH = False


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# REST FRAMEWORK
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
}

# #  This Time Is Used When User Get Token from Refresh Token
# ACCESS_TOKEN_LIFETIME = 6000
# ACCESS_TOKEN_LIFETIME_MOBILE = 6000

# #  This Time Is Used When User Login
# TOKEN_LIFETIME_MOBILE = 36000
# TOKEN_LIFETIME = 36000

# #  This Time Is Used When User First Time login in App/Web
# FIRST_LOGIN_TOKEN_LIFETIME_MOBILE = 6000
# FIRST_LOGIN_TOKEN_LIFETIME = 6000


# # Check if the "logs" directory exists and create it if not
# log_dir = os.path.join(BASE_DIR, "logs")
# if not os.path.exists(log_dir):
#     os.makedirs(log_dir)

