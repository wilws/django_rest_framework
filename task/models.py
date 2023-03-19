from django.db import models
from tile.models import Tile
# Create your models here.


class Task(models.Model):
    
    title = models.CharField(max_length=100)
    order = models.IntegerField()
    description = models.TextField()
    TYPE_CHOICES = (
        ('survey', 'Survey'),
        ('discussion', 'Discussion'),
        ('diary', 'Diary'),
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    tile = models.ForeignKey(Tile, related_name='tasks', on_delete=models.CASCADE)