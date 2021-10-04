from django.contrib.auth.models import AbstractUser
from django.urls.base import reverse


class TMUser(AbstractUser):

    def full_name(self):
        return self.get_full_name()

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)
