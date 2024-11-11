from rest_framework import serializers
from .models import Author, Books

class AuthorSerializer(serializers.Serializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'dob']

class BookSerializer(serializers.Serializer):
    class Meta:
        model = Author
        fields = ['id', 'title', 'author','published_date','genre','is_archived']
