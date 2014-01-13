import os
import sys

from django.conf import settings

location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)
sandbox = lambda x: location("sandbox/{}".format(x))

sys.path.insert(0, sandbox('.'))


def pytest_configure():
    if not settings.configured:
        settings.configure(
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                }
            },
            MEDIA_ROOT=sandbox('public/media'),
            MEDIA_URL='/media/',
            STATIC_URL='/static/',
            STATICFILES_DIRS=[sandbox('static')],
            STATIC_ROOT=sandbox('public/static'),
            STATICFILES_FINDERS=(
                'django.contrib.staticfiles.finders.FileSystemFinder',
                'django.contrib.staticfiles.finders.AppDirectoriesFinder',
            ),
            TEMPLATE_LOADERS=(
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ),
            TEMPLATE_CONTEXT_PROCESSORS = (
                "django.contrib.auth.context_processors.auth",
                "django.core.context_processors.request",
                "django.core.context_processors.debug",
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
                "django.core.context_processors.static",
                "django.contrib.messages.context_processors.messages",
            ),
            MIDDLEWARE_CLASSES=(
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.middleware.locale.LocaleMiddleware',
                'django.middleware.common.CommonMiddleware',
                'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
            ),
            ROOT_URLCONF='sandbox.sandbox.urls',
            TEMPLATE_DIRS=[sandbox('templates')],
            LOGIN_REDIRECT_URL='/accounts/',
            APPEND_SLASH=True,
            SITE_ID=1,
        )
