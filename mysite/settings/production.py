from .base import *
import os

DEBUG = False

# Allow all hosts - Netlify handles domain routing
ALLOWED_HOSTS = ['*']

# Secret key from environment variable
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'temporary-key-change-in-netlify')

# Wagtail-bakery build directory
BUILD_DIR = BASE_DIR / 'build'

# Static files configuration for production with whitenoise
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Add whitenoise
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

# Use whitenoise for static file compression and caching
STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Wagtail-bakery configuration
BAKERY_VIEWS = (
    'wagtailbakery.views.AllPublishedPagesView',
)

try:
    from .local import *
except ImportError:
    pass
