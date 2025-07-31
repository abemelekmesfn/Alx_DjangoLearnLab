import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'relationship_app.settings') 
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)
print("Books by George Orwell:")
for book in books_by_author:
    print(f"- {book.title}")

# List all books in a specific library
library = Library.objects.get(name="Central Library")
library_books = library.books.all()
print(f"\nBooks in {library.name}:")
for book in library_books:
    print(f"- {book.title}")

# Retrieve the librarian for a specific library
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian of {library.name}: {librarian.name}")
