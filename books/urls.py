"""
This file contains URLs for books app.
"""

from rest_framework.routers import DefaultRouter

from .views import BookViewSet

router = DefaultRouter()

router.register(r"books", BookViewSet, basename="book")

urlpatterns = router.urls
