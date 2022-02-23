from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django_tables2 import SingleTableView

from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.statuses.tables import StatusesListTable


class StatusesListView(SingleTableView):
    model = Status
    table_class = StatusesListTable
    template_name = 'statuses/statuses_list.html'


class StatusCreateView(SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses')
    success_message = "Status successfully created"


class StatusChangeView(SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/change.html'
    success_url = reverse_lazy('statuses')
    success_message = "Status successfully changed"


class StatusDeleteView(SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = "Status successfully deleted"
