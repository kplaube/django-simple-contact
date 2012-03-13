# -*- coding: utf-8 -*-

from django.core import mail
from django import forms
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from contact import settings


class ContactForm(forms.Form):
    """
    Sends a contact intent to site administrator.
    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea())

    def send(self, to_email=settings.SITE_EMAIL):
        """
        Send an email message to site administrator with parameters
        filled with form field.
        """
        message = render_to_string('contact/contact_email.html',
            self.cleaned_data)

        return mail.send_mail(
            self.cleaned_data['subject'],
            message,
            self.cleaned_data['email'],
            [to_email, ],
            fail_silently=True,
        )
