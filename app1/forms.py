from django import forms
from app1.models import User,Author,Book
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            


        }



class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields ="__all__"
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),


        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields ="__all__"
        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author_name': forms.Select(attrs={'class': 'form-control'}),
        }