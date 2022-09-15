from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, UpdateView
from django_tables2 import SingleTableView

from task_manager.mixins import AuthorizationRequiredMixin

from .forms import StatusForm
from .models import Status
from .tables import StatusesListTable


class StatusesListView(
    AuthorizationRequiredMixin,
    SingleTableView,
):
    model = Status
    table_class = StatusesListTable
    template_name = 'statuses/statuses_list.html'


class StatusCreateView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _('Status successfully created')


class StatusUpdateView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _('Status successfully updated')


class StatusDeleteView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _('Status successfully deleted')

    def delete(self, request, *args, **kwargs):
        try:
            self.get_object().delete()
        except ProtectedError:
            messages.error(
                self.request,
                _('It is not possible to delete the status because it is being used'),
            )
        else:
            messages.success(
                self.request,
                self.success_message,
            )
        return redirect(self.success_url)
