from django.core import mail
from django.test import TestCase

from contact.forms import ContactForm


class ContactFormTests(TestCase):
    def setUp(self):
        self.parms = {
            'name': 'Bilbo Baggins',
            'email': 'bilbo@themiddleearth.com',
            'subject': 'A ring to rule then all',
            'message': 'Please Gandalf! Help me!',
        }

    def test_send_message(self):
        """
        Should send the message when form is valid.
        """
        form = ContactForm(self.parms)
        self.assertTrue(form.is_valid())

        form.send()
        self.assertEquals(len(mail.outbox), 1)
