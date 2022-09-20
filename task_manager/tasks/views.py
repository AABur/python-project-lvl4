from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableView

from task_manager.mixins import AuthorizationRequiredMixin

from .filters import TaskFilter
from .forms import TaskForm
from .models import Task
from .tables import TasksListTable


class TasksListView(
    AuthorizationRequiredMixin,
    SingleTableView, FilterView,
):
    model = Task
    table_class = TasksListTable
    template_name = 'tasks/tasks_list.html'
    filterset_class = TaskFilter


class TaskCreateView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = _('Task successfully created')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = _('Task successfully updated')


class TaskDeleteView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = _('Task successfully deleted')


class TaskView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    DetailView,
):
    model = Task
    template_name = 'tasks/view_task.html'
