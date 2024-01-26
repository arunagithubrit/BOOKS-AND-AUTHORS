from django import forms
from app1.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)