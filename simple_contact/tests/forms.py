from django.core import mail
from django.test import TestCase

from simple_contact.forms import ContactForm


class ContactFormTests(TestCase):
    def setUp(self):
        self.parms = {
            'name': 'Bilbo Baggins',
            'email': 'bilbo@themiddleearth.com',
            'subject': 'A ring to rule then all',
            'message': 'Please Gandalf! Help me!',
        }

    def test_form_is_valid(self):
        form = ContactForm(self.parms)
        self.assertTrue(form.is_valid())

    def test_sends_the_message(self):
        form = ContactForm(self.parms)
        form.is_valid()

        form.send()

        self.assertEquals(len(mail.outbox), 1)

    def test_cleans_the_message(self):
        self.parms['message'] = '<div><span>Where is Sam?</span></div>'
        form = ContactForm(self.parms)
        form.is_valid()

        expected = "&lt;div&gt;&lt;span&gt;Where is Sam?&lt;/span&gt;&lt;/div&gt;"  # noqa

        self.assertEqual(form.cleaned_data['message'], expected)
