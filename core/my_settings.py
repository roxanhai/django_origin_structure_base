# REST_FRAMEWORK SETTINGS
import datetime

#Setting for API
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER':
        'apps.core.exception_handler.custom_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': [
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '60/min',
    }
}

#Setting for Authentication
SECRET_KEY = "django-insecure-&_de@l^$q5$fj_q7itv*t4f1gnso&w0b!*=n0ghwxywi7(vo%3"
JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_COOKIE': 'JWT',
}
AUTH_USER_MODEL = 'users.User'


# SWAGGER_SETTINGS
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        "Token": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        },
    },
}

# AUTHENTICATION BACKENDS SETTINGS
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'core.authentication_backend.SettingsBackend',
]

#SOCIAL ACCOUNT SETTING
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET= True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_PROVIDERS = {
    'google': { #For Google
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}