
from rest_framework import generics
from .models import Tile
from .serializers import TileSerializer
# Create your views here.


class TileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tile.objects.all()
    serializer_class = TileSerializer
