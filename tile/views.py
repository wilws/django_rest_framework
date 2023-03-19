from rest_framework import generics, viewsets, permissions,authentication
from .models import Tile
from .serializers import TileSerializer
from home.permission import IsStaffEditorPermission


# Testing 
# class TileListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Tile.objects.all()
#     serializer_class = TileSerializer


class TileViewSet(viewsets.ModelViewSet):
    queryset = Tile.objects.all()
    serializer_class = TileSerializer
    authentication_class=[authentication.SessionAuthentication]
    permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]
