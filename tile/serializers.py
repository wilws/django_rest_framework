
from rest_framework import serializers
from .models import Tile

class TileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tile
        fields = [
            'tile_name',
            'launch_date',
            'status',
        ]