from django.db import models

# Create your models here.

"""
Models:
- Author: Stores author names.
- Book: Stores book details and links each book to an author.
Relationship: One author can have many books (One-to-Many via ForeignKey).
"""
# Author model - represents a book author
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name

# Book model - represents a book
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book's title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Link to Author

    def __str__(self):
        return self.title
