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

    def sort_date(obj):
        return obj.this_year

class Post(models.Model):
    author = models.CharField(max_length=256, default='None')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text+' '+self.author

class Comment(models.Model):
    author = models.CharField(max_length=256, default='None')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.text+' '+self.author


class Photo(models.Model):
    author = models.CharField(max_length=256, default='None')
    title = models.CharField(max_length=256, default='None', blank=True, help_text='Title, optional')
    desc = models.TextField(blank=True, help_text='Description, optional')
    date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to = './')

    def __str__(self):
        return self.title+'-----'+self.author

class Phone(models.Model):
    author = models.CharField(max_length=256, default='None')
    phone_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.author
