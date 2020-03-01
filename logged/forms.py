from django.contrib.auth.models import User
from .models import Event
from django.forms import ModelForm
from django import forms

# class AddeventForm(ModelForm):
#     date = forms.DateField(help_text='Use format ')
#
#     class Meta:
#         model = Event
#         fields = ('title','desc', 'date')