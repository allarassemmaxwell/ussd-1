"""
Serializers for the models in the main_app Django application.

These serializers handle the conversion of model instances to JSON format and
the validation of data for creating or updating model instances.
"""

from rest_framework import serializers
from .models import (
    Contact
)


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model.
    """
    class Meta:
        model = Contact
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'message',
            'active',
            'timestamp',
        ]
        read_only_fields = ['id', 'timestamp']
