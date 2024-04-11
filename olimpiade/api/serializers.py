"""Serializers of api app."""
from rest_framework.serializers import ModelSerializer

from tasks.models import Task


class TaskSerializer(ModelSerializer):
    """Task serializer."""

    class Meta:
        """Meta-data of the TaskSerializer class."""

        model = Task
        fields = ('id', 'question', 'answer',)
