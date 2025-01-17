"""
This file contains views for books app.
"""

from datetime import datetime

from bson import ObjectId
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import booksCollection
from .serializers import BookSerializer, YearSerializer


class BookViewSet(viewsets.ViewSet):
    """
    A viewset for books.
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        Get all books.
        """
        books = list(booksCollection.find())
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new book.
        """
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            booksCollection.insert_one(serializer.validated_data)
            return Response("Book created successfully.")
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        """
        Get a book by id.
        """
        pk = ObjectId(pk)
        book = booksCollection.find_one({"_id": pk})
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a book by id.
        """
        updated_book = request.data
        pk = ObjectId(pk)
        book = booksCollection.find_one({"_id": pk})
        if not book:
            return Response("Book not found.", status=404)
        booksCollection.update_one({"_id": pk}, {"$set": updated_book})

        return Response("Book updated successfully.")

    def destroy(self, request, pk=None):
        """
        Delete a book by id.
        """
        pk = ObjectId(pk)
        book = booksCollection.find_one({"_id": pk})
        if not book:
            return Response("Book not found.", status=404)

        booksCollection.delete_one({"_id": pk})
        return Response("Book deleted successfully.")

    @action(detail=False, methods=["get"], url_path="average-price")
    def average_price(self, request):
        """
        Get the average price of all books.
        """
        year = YearSerializer(data=request.query_params)
        year.is_valid(raise_exception=True)
        year = year.validated_data["year"]

        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)

        pipeline = [
            {"$match": {"published_date": {"$gte": start_date, "$lte": end_date}}},
            {"$addFields": {"price": {"$toDouble": "$price"}}},
            {"$group": {"_id": None, "average_price": {"$avg": "$price"}}},
        ]

        result = list(booksCollection.aggregate(pipeline))
        if result:
            return Response({"year": year, "average_price": result[0]["average_price"]})
        return Response({"year": year, "average_price": 0})
