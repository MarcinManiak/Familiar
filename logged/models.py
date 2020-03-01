from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    author = models.CharField(max_length=256, default='None')
    occasion = models.CharField(max_length=64, default='None')
    desc = models.TextField(blank=True)
    day = models.PositiveSmallIntegerField(default=0)
    month = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.occasion+' '+self.author