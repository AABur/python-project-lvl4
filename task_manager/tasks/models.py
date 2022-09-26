from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import TMUser

LENGTH_NAME = 150
LENGTH_DESCRIPTION = 400


class Task(models.Model):
    name = models.CharField(
        unique=True,
        max_length=LENGTH_NAME,
        verbose_name=_('Name'),
    )
    description = models.TextField(
        blank=True,
        max_length=LENGTH_DESCRIPTION,
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

    labels = models.ManyToManyField(
        Label,
        through='LabelsToTask',
        through_fields=('task', 'label'),
        verbose_name=_('Labels'),
    )

    def __str__(self) -> str:
        """Return name of the task."""
        return self.name


class LabelsToTask(models.Model):  # noqa: DJ08
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
    )
    label = models.ForeignKey(
        Label,
        on_delete=models.PROTECT,
    )
