
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    url = serializers.SerializerMethodField(read_only=True)
    tile_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Task
        fields = [
            'title',
            'order',
            'description',
            'type',
            'tile',
            'tile_data',
            'url'
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('task-detail',kwargs={"pk": obj.pk}, request=request)

    
    def get_tile_data(self, obj):
        return {
            'tile_name': obj.tile.tile_name,
            'launch_date': obj.tile.launch_date,
            'status':obj.tile.status,
        }