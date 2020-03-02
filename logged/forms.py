from django.contrib.auth.models import User
from .models import Photo
from django.forms import ModelForm
from django import forms

class ImageForm(ModelForm):
    img = forms.ImageField()

    class Meta:
        model = Photo
        fields = ('img',)