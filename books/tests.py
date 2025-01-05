"""
This file contains tests for books app.
"""

from bson import ObjectId
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from .models import booksCollection


class BookTestCase(TestCase):
    """
    This class defines the test suite for the books app.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.book_data = {
            "title": "Book 1",
            "author": "Author 1",
            "genre": "Genre 1",
            "published_date": "2021-01-01",
            "price": "10.00",
        }

        booksCollection.insert_one(self.book_data)

    def test_get_all_books(self):
        """
        Test to verify that all books are returned.
        """
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, 200)

    def test_create_book(self):
        """
        Test to verify that a book is created.
        """
        new_book_data = {
            "title": "Book 2",
            "author": "Author 2",
            "genre": "Genre 2",
            "published_date": "2021-01-02",
            "price": "20.00",
        }
        response = self.client.post("/api/books/", new_book_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_average_price(self):
        """
        Test to verify that the average price of books is returned.
        """
        response = self.client.get("/api/books/average-price/?year=2021")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"average_price": 20.0, "year": 2021})

    def test_get_book_not_found(self):
        """
        Test to verify that a book is not found.
        """
        random_id = ObjectId()
        response = self.client.get(f"/api/books/{random_id}/")
        self.assertEqual(response.status_code, 404)
