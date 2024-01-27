from rest_framework import serializers
from app1.models import Author,Book


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields="__all__"

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"

