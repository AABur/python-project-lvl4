from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django_tables2 import SingleTableView

from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task
from task_manager.tasks.tables import TasksListTable
from users.models import TMUser


class TasksListView(SingleTableView):
    model = Task
    table_class = TasksListTable
    template_name = 'tasks/tasks_list.html'


class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks')
    success_message = "Task successfully created"

    def form_valid(self, form):
        form.instance.author = TMUser.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)


class TaskChangeView(SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/change.html'
    success_url = reverse_lazy('tasks')
    success_message = "Task successfully changed"


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = "Task successfully deleted"


class TaskView(SuccessMessageMixin, DetailView):
    model = Task
    template_name = 'tasks/view_task.html'


# class TaskView(
#     HandleNoPermissionMixin,
#     LoginRequiredMixin, SuccessMessageMixin,
#     DetailView
# ):
