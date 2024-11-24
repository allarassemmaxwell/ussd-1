"""
models.py

This module defines the Django models for the main_app application.

It includes:
- Custom User model with associated manager for user management.
- Contact model for storing contact form submissions.
- Subscriber model for newsletter subscriptions.
- Testimony model for user testimonials.
- BlogCategory model for blog categories.
- Blog model for individual blog posts.
- BlogComment model for comments on blog posts.

The models utilize Django's built-in fields and functionality to handle
data storage, validation, and relationships.
"""


from __future__ import unicode_literals
import os
from uuid import uuid4
from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _


def path_and_rename(instance, filename):
    """Function to rename file uploaded."""
    upload_to = f'{datetime.now().year}/{datetime.now().month}/'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = f'{instance.pk}.{ext}'
    else:
        filename = f'{uuid4().hex}.{ext}'
    return os.path.join(upload_to, filename)


class Contact(models.Model):
    """
    Model for contact form submissions.
    """
    first_name = models.CharField(
        max_length=255, null=True, blank=True
    )
    last_name = models.CharField(
        max_length=255, null=True, blank=True
    )
    email = models.EmailField(
        max_length=255
    )
    phone_number = models.CharField(
        max_length=255
    )
    message = models.TextField(_("Message"))
    active = models.BooleanField(_("Active"), default=True)
    timestamp = models.DateTimeField(
        _("Created At"), auto_now_add=True
    )
    updated = models.DateTimeField(
        _("Updated At"), auto_now=True
    )

    def __str__(self):
        return str(self.email)

    class Meta:
        ordering = ("-timestamp",)
