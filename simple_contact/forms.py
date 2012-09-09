# -*- coding: utf-8 -*-

import bleach
from django.core.mail import EmailMessage, get_connection
from django import forms
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from simple_contact import settings

connection = get_connection(fail_silently=True)


class ContactForm(forms.Form):
    """
    Sends a contact intent to site administrator.
    """
    name = forms.CharField(label=_('Name'), max_length=100)
    email = forms.EmailField(label=_('Email'))
    subject = forms.CharField(label=_('Subject'), max_length=255)
    message = forms.CharField(label=_('Message'), widget=forms.Textarea())

    def send(self, to_email=settings.SITE_EMAIL):
        """
        Send an email message to site administrator with parameters
        filled with form field.
        """
        self.cleaned_data['message'] = bleach.clean(
            self.cleaned_data['message'],
            tags=settings.ALLOWED_TAGS,
            attributes=settings.ALLOWED_ATTRIBUTES,
            strip_comments=True,
        )

        message = render_to_string('simple_contact/contact_email.html',
            self.cleaned_data)
        connection.open()

        mail = EmailMessage(
            self.cleaned_data['subject'],
            message,
            self.cleaned_data['email'],
            [to_email, ],
            connection=connection,
        )
        mail.content_subtype = 'html'
        mail.send()
