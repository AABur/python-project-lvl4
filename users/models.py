from django.contrib.auth.models import AbstractUser


class TMUser(AbstractUser):

    def full_name(self):
        return self.get_full_name()
