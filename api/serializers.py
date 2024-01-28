from rest_framework import serializers
from app1.models import Author,Book


class AuthorListSerializer(serializers.ModelSerializer):
    total_authors=serializers.CharField(read_only=True)
    class Meta:
        model=Author
        fields="__all__"

class BookListSerializer(serializers.ModelSerializer):
    total_books=serializers.CharField(read_only=True)
    class Meta:
        model=Book
        fields="__all__"

