
from rest_framework import serializers
from .models import Tile


class TileSerializer(serializers.ModelSerializer):

    tasks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='task-detail'
    )

    class Meta:
        model = Tile
        fields = [
            'tile_name',
            'launch_date',
            'status',
            'tasks'
        ]

