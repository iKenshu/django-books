"""
This file contains initial data for books app.
"""

from datetime import datetime

from django.core.management.base import BaseCommand

from books.models import booksCollection
from books.serializers import BookSerializer


class Command(BaseCommand):
    """
    A class to define the command to load initial data.
    """

    help = "Load initial data for books app."

    def handle(self, *args, **options):
        """
        A method to load initial data.
        """
        books_data = [
            {
                "title": "El Alquimista",
                "author": "Paulo Coelho",
                "genre": "Ficción",
                "price": "15.99",
                "published_date": datetime(1988, 1, 1),
            },
            {
                "title": "Cien Años de Soledad",
                "author": "Gabriel García Márquez",
                "genre": "Realismo Mágico",
                "price": "12.50",
                "published_date": datetime(1967, 5, 30),
            },
            {
                "title": "1984",
                "author": "George Orwell",
                "genre": "Distopía",
                "price": "8.99",
                "published_date": datetime(1949, 6, 8),
            },
            {
                "title": "La Sombra del Viento",
                "author": "Carlos Ruiz Zafón",
                "genre": "Misterio",
                "price": "10.99",
                "published_date": datetime(2001, 1, 1),
            },
            {
                "title": "Orgullo y Prejuicio",
                "author": "Jane Austen",
                "genre": "Romántico",
                "price": "9.99",
                "published_date": datetime(1813, 1, 28),
            },
            {
                "title": "Brida",
                "author": "Paulo Coelho",
                "genre": "Ficción",
                "price": "14.99",
                "published_date": datetime(1988, 6, 1),
            },
            {
                "title": "Crónica de una Muerte Anunciada",
                "author": "Gabriel García Márquez",
                "genre": "Realismo Mágico",
                "price": "13.99",
                "published_date": datetime(1967, 8, 15),
            },
            {
                "title": "Animal Farm",
                "author": "George Orwell",
                "genre": "Distopía",
                "price": "9.99",
                "published_date": datetime(1949, 11, 17),
            },
            {
                "title": "El Juego del Ángel",
                "author": "Carlos Ruiz Zafón",
                "genre": "Misterio",
                "price": "18.99",
                "published_date": datetime(2001, 5, 23),
            },
            {
                "title": "Emma",
                "author": "Jane Austen",
                "genre": "Romántico",
                "price": "11.49",
                "published_date": datetime(1813, 12, 25),
            },
        ]

        for book_data in books_data:
            book_serializer = BookSerializer(data=book_data)
            if book_serializer.is_valid():
                booksCollection.insert_one(book_serializer.validated_data)
            else:
                print(f"Error: {book_serializer.errors}")

        print(f"{len(books_data)} books loaded successfully.")
