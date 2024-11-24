"""
Configuration for the main app.

This module contains the application configuration for the `main_app` Django app,
including the custom AppConfig class that specifies settings related to the app.
"""

from django.apps import AppConfig


class MainAppConfig(AppConfig):
    """
    Configuration for the MainApp Django application.

    This class defines settings specific to the `main_app` application, including
    setting the default auto field and importing signals when the app is ready.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "main_app"
