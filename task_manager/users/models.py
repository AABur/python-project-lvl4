"""Represents TMUser objects in the database."""

from django.contrib.auth.models import AbstractUser


class TMUser(AbstractUser):
    """Represents TMUser objects in the database."""

    def __str__(self):
        """Represent the TMUser object."""
        return f'{self.last_name}, {self.first_name}'

    def full_name(self):
        """Return the full name of the user."""
        return self.get_full_name()
