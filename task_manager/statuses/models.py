from django.db import models


class Status(models.Model):
    name = models.CharField(unique=True, max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
