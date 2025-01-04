"""
This file contains models for books app.
"""

from django.db import models

from books.utils import get_db


class Book(models.Model):
    """
    A model to represent a book.
    """

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title


db = get_db()
booksCollection = db["books"]
