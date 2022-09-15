from django.forms.widgets import CheckboxInput
from django.utils.translation import gettext as _
from django_filters import BooleanFilter, FilterSet, ModelChoiceFilter

from labels.models import Label

from .models import Task


# MY
class TaskFilter(FilterSet):
    label = ModelChoiceFilter(queryset=Label.objects.all(), label=_('Label'))

    self_tasks = BooleanFilter(
        widget=CheckboxInput,
        method="filter_self_tasks",
        label=_('Only your tasks')
    )

    def filter_self_tasks(self, queryset, name, value):
        return queryset.filter(author=self.request.user) if value else queryset

    class Meta:
        model = Task
        fields = ["status", "executor", "labels"]
