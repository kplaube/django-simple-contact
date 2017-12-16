from django.core import mail
from django.test import TestCase
from django.urls import reverse


class ContactViewsTests(TestCase):
    urls = 'simple_contact.urls'

    def test_contact_view(self):
        """
        Ensure that contact view can respond to GET and POST.
        """

        # Get
        response = self.client.get(reverse('contact-contact'))
        self.assertEquals(response.status_code, 200)

        # Post an invalid form
        response = self.client.post(reverse('contact-contact'), {})
        self.assertEquals(response.status_code, 200)

        # Post
        response = self.client.post(reverse('contact-contact'), {
            'name': 'Gandalf',
            'email': 'gandalf@themiddleearth.com',
            'subject': 'Let\'s go to an adventure!',
            'message': 'C\'mon Bilbo! Let\'s do it!',
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(len(mail.outbox), 1)
