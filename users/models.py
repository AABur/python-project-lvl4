"""Represents TMUser objects in the database."""
from django.contrib.auth.models import AbstractUser
from django.urls.base import reverse


class TMUser(AbstractUser):
    """Represents TMUser objects in the database."""

    def __str__(self):
        """Represent the TMUser object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)

    def get_absolute_url(self):
        """Return the url to access a particular author instance."""
        return reverse('user-detail', args=[str(self.id)])

    def full_name(self):
        """Return the full name of the user."""
        return self.get_full_name()
