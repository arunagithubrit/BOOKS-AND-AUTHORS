from django.shortcuts import render
from api.serializers import AuthorListSerializer,BookListSerializer
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from app1.models import Author,Book

class AuthorListView(ModelViewSet):
    serializer_class=AuthorListSerializer
    model=Author
    queryset=Author.objects.all()

class BookListView(ModelViewSet):
    serializer_class=BookListSerializer
    model=Book
    queryset=Book.objects.all()
