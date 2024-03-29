from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-%-4qk=7j!&!+vv(0+cysbq!_3_0ks!m%a4)!)d+6=6jb-8%ndn'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		'oauth2_provider',
		'corsheaders',
		'rest_framework',
		'mineauth',
]
CRISPY_ALLOWED_TEMPLATE_PACKS = (
		'bootstrap', 'uni_form', 'bootstrap3', 'foundation-5', 'bootstrap4')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
		'django.middleware.security.SecurityMiddleware',
		'django.contrib.sessions.middleware.SessionMiddleware',
		'oauth2_provider.middleware.OAuth2TokenMiddleware',
		'corsheaders.middleware.CorsMiddleware',
		'django.middleware.common.CommonMiddleware',
		'django.middleware.csrf.CsrfViewMiddleware',
		'django.contrib.auth.middleware.AuthenticationMiddleware',
		# 'oauth2_provider.backends.OAuth2Backend',
		'django.contrib.messages.middleware.MessageMiddleware',
		'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oauthlibme.urls'

TEMPLATES = [
		{
				'BACKEND' : 'django.template.backends.django.DjangoTemplates',
				'DIRS'    : [],
				'APP_DIRS': True,
				'OPTIONS' : {
						'context_processors': [
								'django.template.context_processors.debug',
								'django.template.context_processors.request',
								'django.contrib.auth.context_processors.auth',
								'django.contrib.messages.context_processors.messages',
						],
				},
		},
]

WSGI_APPLICATION = 'oauthlibme.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
		'default': {
				'ENGINE': 'django.db.backends.sqlite3',
				'NAME'  : BASE_DIR / 'db.sqlite3',
		}
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
		'DEFAULT_AUTHENTICATION_CLASSES': (
				'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
		),
		'DEFAULT_PERMISSION_CLASSES'    : (
				'rest_framework.permissions.AllowAny',
		
		)
}

with open('oidc.key', 'r') as f:
	OIDC_RSA_PRIVATE_KEY = f.read()

OAUTH2_PROVIDER = {
		"ACCESS_TOKEN_EXPIRE_SECONDS": 6000,
		# AUTHORIZATION_CODE_EXPIRE_SECONDS:'',
		"OIDC_ENABLED"               : True,
		"OIDC_RSA_PRIVATE_KEY"       : OIDC_RSA_PRIVATE_KEY,
		"PKCE_REQUIRED"              : True,
		'SCOPES'                     : {
				"openid": "OpenID Connect scope",
				'read'  : 'Read scope',
				'write' : 'Write scope',
				'groups': 'Access to your groups'
		},
		# "OIDC_RSA_PRIVATE_KEYS_INACTIVE": [
		# 		os.environ.get("OIDC_RSA_PRIVATE_KEY_2"),
		# 		os.environ.get("OIDC_RSA_PRIVATE_KEY_3")
		# ]
}
