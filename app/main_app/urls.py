"""
URL configurations for the MainApp Django application.
"""

from django.urls import path
from .views import (
    ContactCreateView, ussd_menu
)

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact_create'),
    path('ussd/', ussd_menu, name='ussd_menu'),
]
