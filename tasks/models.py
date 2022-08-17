from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import TMUser
from statuses.models import Status


class Task(models.Model):
    name = models.CharField(
        unique=True,
        max_length=150,
        verbose_name=_('Name'),
    )
    description = models.TextField(
        blank=True,
        max_length=400,
        verbose_name=_('Description'),
    )
    author = models.ForeignKey(
        TMUser,
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name=_('Author'),
    )
    executor = models.ForeignKey(
        TMUser,
        on_delete=models.PROTECT,
        related_name='executor',
        verbose_name=_('Executor'),
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name=_('Status'),
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Creation date'),
    )

    def __str__(self) -> str:
        return self.name
