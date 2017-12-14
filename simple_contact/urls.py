from django.urls import path
from simple_contact.views import ContactView

urlpatterns = [
    path('', ContactView.as_view(), name='contact-contact'),
]
