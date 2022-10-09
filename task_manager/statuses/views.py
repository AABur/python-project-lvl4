from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, UpdateView
from django_tables2 import SingleTableView

from task_manager.mixins import AuthorizationRequiredMixin
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.statuses.tables import StatusesListTable


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
    template_name = 'common_form.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _('Status successfully created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = _('Create status')
        context['form_button'] = _('Create')
        return context


class StatusUpdateView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = Status
    form_class = StatusForm
    template_name = 'common_form.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _('Status successfully updated')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = _('Change status')
        context['form_button'] = _('Change')
        return context


class StatusDeleteView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Status
    template_name = 'delete.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _('Status successfully deleted')

    def delete(self, request, *args, **kwargs):
        """Override delete method to handle ProtectedError exception."""
        try:
            self.get_object().delete()
        except ProtectedError:
            messages.error(
                self.request,
                _('It is not possible to delete the status because it is being used'),  # noqa: E501
            )
        else:
            messages.success(
                self.request,
                self.success_message,
            )
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete status')
        return context
