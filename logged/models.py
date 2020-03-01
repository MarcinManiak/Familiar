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

class Post(models.Model):
    author = models.CharField(max_length=256, default='None')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text+' '+self.author

class Comment(models.Model):
    author = models.CharField(max_length=256, default='None')
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.post+'-----'+self.comment