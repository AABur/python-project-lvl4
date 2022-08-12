from django.db import models

from users.models import TMUser
from task_manager.statuses.models import Status


class Task(models.Model):
    name = models.CharField(
        unique=True,
        max_length=150,
    )
    description = models.TextField(
        blank=True,
        max_length=400,
    )
    author = models.ForeignKey(
        TMUser,
        on_delete=models.PROTECT,
        related_name='author',
    )
    executor = models.ForeignKey(
        TMUser,
        on_delete=models.PROTECT,
        related_name='executor',
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return self.name
