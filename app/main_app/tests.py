"""
Test cases for the main app, covering API endpoints and models.

This module includes unit tests for the views, serializers, and models of
the main app. The tests verify the functionality of various features,
including the creation, retrieval, and manipulation of data related to
subscribers, blogs, testimonies, donations, volunteers, and other entities.
"""


from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from .models import (
    Contact
)

class ContactAPITest(TestCase):
    """
    Test case for the Contact API endpoints.
    This class tests the creation and validation of Contact objects through the API.
    """
    def setUp(self):
        self.client = APIClient()
        self.contact_url = reverse('contact_create')

    def test_create_contact(self):
        """
        Ensure we can create a new Contact object via the API.
        """
        data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'janedoe@example.com',
            'phone_number': '0987654321',
            'message': 'This is another test message.',
            'active': True
        }

        response = self.client.post(self.contact_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 1)
        # Now assert the created object
        contact = Contact.objects.get()
        self.assertEqual(contact.first_name, 'Jane')
        self.assertEqual(contact.last_name, 'Doe')

    def test_create_contact_invalid_data(self):
        """
        Ensure that invalid data results in a bad request response.
        """
        invalid_data = {
            'first_name': '',
            'last_name': '',
            'email': 'invalidemail',
            'phone_number': '',
            'message': ''
        }

        response = self.client.post(self.contact_url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Contact.objects.count(), 0)
