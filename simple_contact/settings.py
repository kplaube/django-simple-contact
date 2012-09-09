import bleach
from django.conf import settings

SITE_EMAIL = getattr(settings, 'SITE_EMAIL', 'site@mail.com')

ALLOWED_TAGS = [
    'p',
] + bleach.ALLOWED_TAGS

ALLOWED_ATTRIBUTES = bleach.ALLOWED_ATTRIBUTES.copy()
ALLOWED_ATTRIBUTES.update({
    'a': ['href', 'title', 'rel', 'target'],
})
