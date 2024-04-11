"""URL configuration for api app."""
from django.urls import path

from .constants import API_VERSION

urlpatterns = [
    path(f'{API_VERSION}/', ...),
]
