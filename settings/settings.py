import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = "{{ secret_key }}"

DEBUG = False
ALLOWED_HOSTS = []
ADMINS = (
    # ('Ivan Lukyanets', 'ivan@il-studio.ru'),
)

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

THIRD_APPS = [
    #
]

CUSTOM_APPS = [
    'applications.core',
    'applications.main',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + CUSTOM_APPS + ['django_cleanup']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'applications.main.processors.preference',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True
SITE_ID = 1

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'static_nginx')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

if os.getenv('EMAIL_HOST'):
    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
    DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
    EMAIL_PORT = os.getenv('EMAIL_PORT')

# CKEDITOR
# https://github.com/django-ckeditor/django-ckeditor

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            [
                'Format',
                'Bold',
                'Italic',
                'Underline',
                'Strike',
                'SpellChecker',
            ],
            [
                'Blockquote',
                'RemoveFormat',
            ],
            [
                'NumberedList',
                'BulletedList',
                'Indent',
                'Outdent',
                'JustifyLeft',
                'JustifyCenter',
                'JustifyRight',
                'JustifyBlock',
            ],
            [
                'Image',
                'Table',
                'Link',
                'Unlink',
                'Anchor',
                'SectionLink',
                'Subscript',
                'Superscript',
            ],
            [
                'Undo',
                'Redo',
            ],
            [
                'Embed',
                'Iframe',
            ],
            [
                'Source',
            ],
            [
                'Maximize',
            ],
        ],
        'width':
        '100%',
        'extraPlugins':
        ','.join([
            'embed',
            'iframe',
        ]),
        'extraAllowedContent':
        'div(col-xs-*,col-sm-*,col-md-*,col-lg-*,container,container-fluid,row,ratio*); small',
    },
}

try:
    from .local_settings import *  # pylint: disable=wildcard-import
except ImportError:
    pass
