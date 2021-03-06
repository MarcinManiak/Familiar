from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Family
from django.forms import ModelForm
from django import forms
User._meta.get_field('email')._unique = True

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class CreateFamily(ModelForm):
    class Meta:
        model = Family
        fields = ('name','description')

