from django.db import models

# Create your models here.


class Tile(models.Model):
    tile_name = models.CharField(max_length=100, blank=True, null=True)
    launch_date = models.DateField()
    STATUS_CHOICES = (
        ('live', 'Live'),
        ('pending', 'Pending'),
        ('archived', 'Archived'),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)