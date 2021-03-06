from base.settings.base import *
import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# For extra security --run python manage.py check --deploy

CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True


ALLOWED_HOSTS = ['.hairwayskenya.com']

INSTALLED_APPS.append(
    'storages'
)

# SENTRY SETUP
SENTRY_KEY = os.getenv('SENTRY_KEY')
SENTRY_ORG = os.getenv('SENTRY_ORG')
SENTRY_PROJECT = os.getenv('SENTRY_PROJECT')

sentry_sdk.init(
    dsn=f"https://{SENTRY_KEY}@{SENTRY_ORG}.ingest.sentry.io/{SENTRY_PROJECT}",
    integrations=[DjangoIntegration()],

    # To associate users to errors
    send_default_pii=True)


# Email
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

# AWS
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# Media
DEFAULT_FILE_STORAGE = 'base.settings.storage_backends.MediaStorage'

# Static
STATIC_ROOT = os.path.join(BASE_DIR,
                           f'/home/{HOST_USERNAME}/hairways/static')
