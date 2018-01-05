DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}
SECRET_KEY = 'dsl'
INSTALLED_APPS = [
    'django.contrib.messages',
    'simple_contact'
]
ROOT_URLCONF = 'simple_contact.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
    }
]
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]
MIDDLEWARE_CLASSES = MIDDLEWARE  # For Django 1.8 support
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
