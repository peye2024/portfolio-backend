# import os
# import dj_database_url
# from decouple import config
# from pathlib import Path
#
# BASE_DIR = Path(__file__).resolve().parent.parent.parent
# SECRET_KEY = config('SECRET_KEY')
# DEBUG = True
# ALLOWED_HOSTS = []
#
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'rest_framework.authtoken',
#     'rest_framework',
#     'django_filters',
#     'corsheaders',
#     'drf_spectacular',
#     'django.contrib.staticfiles',
#     'coreapp.apps.CoreappConfig',
#     'project.apps.ProjectConfig',
#     'articles.apps.ArticlesConfig',
#     'utilities.apps.UtilitiesConfig',
#
# ]
#
# MIDDLEWARE = [
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'Config.middleware.CustomMiddleWare',
# ]
#
# ROOT_URLCONF = 'Config.urls'
#
# # noinspection PyUnresolvedReferences
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'Config.wsgi.application'
#
# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#     'PAGE_SIZE': 30,
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.TokenAuthentication',
#     ],
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ],
#     'DEFAULT_FILTER_BACKENDS': (
#         'django_filters.rest_framework.DjangoFilterBackend',
#     ),
#     'DEFAULT_RENDERER_CLASSES': [
#         'coreapp.renderers.CustomRenderer',
#     ],
#     'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
#     # 'EXCEPTION_HANDLER': 'Config.api.exceptions.api_500_handler',
#
# }
#
# SPECTACULAR_SETTINGS = {
#     'TITLE': 'Portfolio API',
#     'DESCRIPTION': 'Portfolio API for managing projects, blogs, and related information',
#     'VERSION': '1.0.0',
#     'SCHEMA_PATH_PREFIX': '/api/v[0-9]',
#     'SERVE_INCLUDE_SCHEMA': False,
#     'CONTACT': {
#         'name': 'Mahmudul Hasan',
#         'email': 'hasaanshimul@gmail.com',
#         'url': 'https://www.yourportfolio.com',
#         'phone': '+8801713914899'
#     },
#
# }
#
# # Database
# # https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# # Check Production and development script for clear understanding.
#
#
# # Password validation
# # https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
# # Internationalization
# # https://docs.djangoproject.com/en/5.1/topics/i18n/
# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_TZ = True
#
# # Default primary key field type
# # https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
#
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024
# AUTH_USER_MODEL = 'coreapp.User'
#
# CORS_ALLOW_ALL_ORIGINS = True
# CSRF_TRUSTED_ORIGINS = [
#     'https://*.*',
#     'http://*.*',
#     'http://localhost:5174/'
# ]
# MEDIA_HOST = config('MEDIA_HOST')
#
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = config('EMAIL_PORT', cast=int)
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_USE_SSL = True
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'