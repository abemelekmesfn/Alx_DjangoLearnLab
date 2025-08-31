from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

"""
Serializers:
- BookSerializer: Serializes Book model and validates publication year.
- AuthorSerializer: Serializes Author and includes a nested list of books written by the author.
Nesting: BookSerializer is nested inside AuthorSerializer using the `books` related name.
"""
# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    # Nesting BookSerializer to include books written by the author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
