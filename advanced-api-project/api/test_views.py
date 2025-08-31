from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Book, Author

"""
Tests:
- Create, Update, and Delete operations with and without authentication
- Filtering by author ID
- Searching by title
- Ordering by publication year
"""

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create user for authenticated requests
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create authors
        self.author1 = Author.objects.create(name="George Orwell")
        self.author2 = Author.objects.create(name="J.K. Rowling")

        # Create books
        self.book1 = Book.objects.create(title="1984", publication_year=1949, author=self.author1)
        self.book2 = Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author1)
        self.book3 = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author2)

        self.create_url = reverse("book-create")
        self.list_url = reverse("book-list")
        self.detail_url = lambda pk: reverse("book-detail", kwargs={"pk": pk})
        self.update_url = lambda pk: reverse("book-update", kwargs={"pk": pk})
        self.delete_url = lambda pk: reverse("book-delete", kwargs={"pk": pk})

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author1.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2020,
            "author": self.author1.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.put(self.update_url(self.book1.pk), {
            "title": "1984 - Updated",
            "publication_year": 1949,
            "author": self.author1.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "1984 - Updated")

    def test_update_book_unauthenticated(self):
        response = self.client.put(self.update_url(self.book1.pk), {
            "title": "Should Fail",
            "publication_year": 1949,
            "author": self.author1.id
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(self.delete_url(self.book2.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book2.pk).exists())

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {'author': self.author1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url, {'search': 'Harry'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter")

    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
