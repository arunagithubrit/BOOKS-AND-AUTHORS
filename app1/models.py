from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=100)
    user_name=models.CharField(max_length=100)
    
    email = models.EmailField(unique=True)
    status=models.BooleanField(default=True)
    # Add other Author fields as needed

    def __str__(self):
        return self.author_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    created_date = models.DateField()
    status=models.BooleanField(default=True)
    # Add other Book fields as needed

    def __str__(self):
        return self.title