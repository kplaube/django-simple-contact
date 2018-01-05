from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView

try:
    from django.urls import reverse
except ImportError:  # Django 1.8 support
    from django.core.urlresolvers import reverse

from simple_contact.forms import ContactForm


class ContactView(FormView):
    """
    Displays the contact form and handles validation and email
    submission.
    """
    form_class = ContactForm
    template_name = 'simple_contact/contact_form.html'

    def form_valid(self, form):
        form.send()
        messages.success(
            self.request,
            _('Your message was sent successfully! Thank you.')
        )

        return super(ContactView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            _('Oops! Are you sure that the form was filled out correctly?')
        )

        return super(ContactView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('contact-contact')
