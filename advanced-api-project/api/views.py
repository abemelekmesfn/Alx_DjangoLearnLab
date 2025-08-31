from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import filters 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from datetime import datetime

# BookListView: Handles GET requests to list all books
# BookDetailView: Handles GET requests for a specific book by ID
# BookCreateView: Handles POST requests to create a book (requires auth)
# BookUpdateView: Handles PUT/PATCH requests to update a book (requires auth)
# BookDeleteView: Handles DELETE requests to delete a book (requires auth)

# Create your views here.

# BookListView:
# - Supports filtering by title, author ID, and publication year.
# - Allows searching by title or author's name.
# - Supports ordering by title or publication year (ascending or descending).
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching
    search_fields = ['title', 'author__name']

    # Ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


# DetailView: Retrieve a single book by ID (GET only)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Open to all users


# CreateView: Add a new book (POST)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only
    
    def perform_create(self, serializer):
        # Add extra logic if needed (e.g., log creation)
        print("Creating a book:", serializer.validated_data)
        serializer.save()

# UpdateView: Modify an existing book (PUT/PATCH)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only


# DeleteView: Remove a book (DELETE)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only