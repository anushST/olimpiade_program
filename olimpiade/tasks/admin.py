"""Admin-zone setting for tasks app."""
from django.contrib import admin

from .models import Task

admin.site.register(Task)
