from django.forms.widgets import CheckboxInput
from django.utils.translation import gettext as _
from django_filters import BooleanFilter, FilterSet, ModelChoiceFilter

from task_manager.labels.models import Label
from task_manager.tasks.models import Task


# MY
class TaskFilter(FilterSet):
    label = ModelChoiceFilter(queryset=Label.objects.all(), label=_('Label'))

    self_tasks = BooleanFilter(
        widget=CheckboxInput,
        method='filter_self_tasks',
        label=_('Only your tasks'),
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def filter_self_tasks(self, queryset, name, value):  # noqa: WPS110
        """Filter tasks by current user."""
        return queryset.filter(author=self.request.user) if value else queryset
