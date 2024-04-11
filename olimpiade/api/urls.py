"""URL configuration for api app."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .constants import API_VERSION
from .views import TaskViewSet

router = DefaultRouter()
router.register('', TaskViewSet)

urlpatterns = [
    path(f'{API_VERSION}/', include(router.urls)),
]
