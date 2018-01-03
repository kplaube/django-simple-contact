from django.core import mail
from django.test import TestCase
from django.urls import reverse


class ContactViewsTests(TestCase):
    urls = 'simple_contact.urls'

    def test_successfully_access_the_form(self):
        response = self.client.get(reverse('contact-contact'))
        self.assertEquals(response.status_code, 200)

    def test_sends_a_message_by_doing_a_post(self):
        response = self.client.post(reverse('contact-contact'), {
            'name': 'Gandalf',
            'email': 'gandalf@themiddleearth.com',
            'subject': 'Let\'s go to an adventure!',
            'message': 'C\'mon Bilbo! Let\'s do it!',
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(len(mail.outbox), 1)

    def test_does_not_send_a_message_when_form_is_invalid(self):
        response = self.client.post(reverse('contact-contact'), {})

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(mail.outbox), 0)
