"""
This file contains commands to create test users.
"""

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    A command to create test users.
    """

    help = "Create test users."

    def handle(self, *args, **options):
        """
        Create test users.
        """
        test_users = [
            {"username": "user1", "password": "password1", "email": "test@email.com"},
            {"username": "user2", "password": "password2", "email": "test@email1.com"},
        ]

        for user_data in test_users:
            user, created = User.objects.get_or_create(
                username=user_data["username"],
                email=user_data["email"],
            )
            if created:
                user.set_password(user_data["password"])
                user.save()
                self.stdout.write(self.style.SUCCESS(f"User {user.username} created."))
            else:
                self.stdout.write(
                    self.style.WARNING(f"User {user.username} already exists.")
                )
