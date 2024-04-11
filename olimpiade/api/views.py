"""Views of api app."""
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from .serializers import TaskSerializer
from tasks.models import Task


class TaskViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    """Task view set.

    GET(list): returns the last Task object's data
    POST: create Task object
    Other method: Not Allowed
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        """Return json when requested GET method (list_action).

        Ovverided to return last Task's data.
        """
        last_task = Task.objects.last()
        serializer = TaskSerializer(last_task)
        return Response(serializer.data, HTTP_200_OK)
