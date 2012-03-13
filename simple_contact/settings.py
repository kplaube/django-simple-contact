from django.conf import settings

SITE_EMAIL = getattr(settings, 'SITE_EMAIL', 'site@mail.com')
