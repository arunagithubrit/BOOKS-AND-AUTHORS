from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=100)
    user_name=models.CharField(max_length=100)
    
    email = models.EmailField(unique=True)
    status=models.BooleanField(default=True)
   

    def __str__(self):
        return self.author_name
    
    @property
    def total_authors(self):
        num_authors = Author.objects.count()
        return num_authors
    
# if __name__ == "__main__":
#     num_authors, num_books = total_author_books()
#     print(f"Number of Authors: {num_authors}")
#     print(f"Number of Books: {num_books}")



    

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_id=models.CharField(max_length=100,null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    created_date = models.DateField(auto_now_add=True,null=True)
    status=models.BooleanField(default=True)
    # Add other Book fields as needed

    def __str__(self):
        return self.book_name
    
    @property
    def total_books(self):
        num_books = Book.objects.count()
        return num_books
    