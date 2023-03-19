from rest_framework import generics, viewsets, permissions,authentication
from .models import Task
from .serializers import TaskSerializer
from home.permission import IsStaffEditorPermission

# Create your views here.

# For testing the connection 
# class TaskListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_class=[authentication.SessionAuthentication]
    permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]

                     

