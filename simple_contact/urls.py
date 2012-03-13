from django.conf.urls.defaults import patterns, url
from simple_contact.views import ContactView

urlpatterns = patterns('',
    url(r'^$', ContactView.as_view(), name='contact-contact'),
)
