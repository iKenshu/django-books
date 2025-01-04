"""
This file contains mongo database settings.
"""

from pymongo import MongoClient

from django_books.settings import MONGO_URI


def get_db():
    """
    Get the mongo database.
    """
    client = MongoClient(MONGO_URI)
    db = client["books_db"]
    return db
