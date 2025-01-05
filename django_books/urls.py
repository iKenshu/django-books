"""
django_books URL Configuration
"""

from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Books API",
        default_version="v1",
        description="A simple API to manage books.",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("books.urls"), name="books"),
    path("api-token-auth/", obtain_auth_token),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(
        "swagger<format>",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
]
