from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    name = models.CharField(
        unique=True,
        max_length=100,
        verbose_name=_('Name'),
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Creation date'),
    )

    def __str__(self) -> str:
        """Return name of the status."""
        return self.name
