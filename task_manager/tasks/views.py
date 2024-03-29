from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from task_manager.mixins import AuthorizationRequiredMixin
from task_manager.tasks.filters import TaskFilter
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task
from task_manager.tasks.tables import TasksListTable


class TasksListView(
    AuthorizationRequiredMixin,
    SingleTableMixin,
    FilterView,
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
    template_name = 'common_form.html'
    success_url = reverse_lazy('tasks:list')
    success_message = _('Task successfully created')

    def form_valid(self, form):
        """Override form_valid method to set task author to current user."""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Return context data for template."""
        context = super().get_context_data(**kwargs)
        context['form_title'] = _('Create task')
        context['form_button'] = _('Create')
        return context


class TaskUpdateView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = Task
    form_class = TaskForm
    template_name = 'common_form.html'
    success_url = reverse_lazy('tasks:list')
    success_message = _('Task successfully updated')

    def get_context_data(self, **kwargs):
        """Return context data for template."""
        context = super().get_context_data(**kwargs)
        context['form_title'] = _('Change task')
        context['form_button'] = _('Change')
        return context


class TaskDeleteView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('tasks:list')
    success_message = _('Task successfully deleted')

    def get_context_data(self, **kwargs):
        """Return context data for template."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete task')
        return context


class TaskView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    DetailView,
):
    model = Task
    template_name = 'tasks/view_task.html'
