from django.conf.urls import url

from simple_contact.views import ContactView

urlpatterns = [
    url(r'^$', ContactView.as_view(), name='contact-contact'),
]
