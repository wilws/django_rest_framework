from django.urls import path
from . import views

# /api/tile
urlpatterns = [
    path('',views.TaskListCreateAPIView.as_view())
]