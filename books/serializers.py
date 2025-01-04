"""
This file contains serializers for books app.
"""

from datetime import date, datetime

from bson import ObjectId
from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    """
    This class defines the serializer for Book model.
    """

    _id = serializers.CharField(max_length=100, required=False, read_only=True)
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    genre = serializers.CharField(max_length=100)
    published_date = serializers.DateTimeField(format="%Y-%m-%d", default=date.today)
    price = serializers.CharField(max_length=5)

    def create(self, validated_data):
        """
        Method to use the validated data to create a new book.
        """
        if "_id" not in validated_data:
            validated_data["_id"] = str(ObjectId())

        validated_data["published_date"] = datetime.combine(
            validated_data["published_date"], datetime.min.time()
        )

        return validated_data

    def to_representation(self, instance):
        """
        Convert MongoDB document to Python dictionary.
        """
        representation = super().to_representation(instance)
        published_date = representation.get("published_date")
        if isinstance(representation.get("published_date"), datetime):
            representation["published_date"] = published_date.date()
        return representation

    def to_internal_value(self, data):
        """
        Convert published date string to date object.
        """
        data = super().to_internal_value(data)
        if isinstance(data.get("published_date"), str):
            try:
                data["published_date"] = datetime.strptime(
                    data["published_date"], "%Y-%m-%d"
                ).date()
            except ValueError:
                raise serializers.ValidationError(
                    "Invalid date format. Use YYYY-MM-DD."
                )
        return data
