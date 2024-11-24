"""
Views for handling various HTTP requests and responses related to subscribers,
testimonies, blogs, comments, donations, volunteers, and more in the main app.

This module contains Django REST framework views that interact with the database
models such as Subscriber, Blog, Partner, Volunteer, and Donation, among others.

Each view is implemented as a class-based view that provides a specific endpoint
for interacting with the app's data.
"""

from rest_framework import generics

from .models import (
    Contact
)
from .serializers import (
    ContactSerializer
)


class ContactCreateView(generics.CreateAPIView):
    """
    Handle POST requests for Contact.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
