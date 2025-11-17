# songil-django/backend/tasks/urls.py
from django.urls import path
from .views import NearbyTaskListView

urlpatterns = [
    # GET /api/v1/tasks/nearby/
    path('nearby/', NearbyTaskListView.as_view(), name='task-nearby-list'),
]