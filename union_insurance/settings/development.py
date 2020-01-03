from .base import *
SECRET_KEY = '5n@_$tgyve8=(oo)no1ys8h%=mto!a!r1tq%-9!)&g-z6o9fso'
DEBUG = True
ALLOWED_HOSTS += ['*']

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# DEBUG TOOLBAR SETTINGS

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/unionstatic/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
MEDIA_URL = '/unionmedia/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')