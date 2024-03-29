from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, UpdateView
from django_tables2 import SingleTableView

from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label
from task_manager.labels.tables import LabelsListTable
from task_manager.mixins import AuthorizationRequiredMixin


class LabelsListView(
    AuthorizationRequiredMixin,
    SingleTableView,
):
    model = Label
    table_class = LabelsListTable
    template_name = 'labels/labels_list.html'


class LabelCreateView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    model = Label
    form_class = LabelForm
    template_name = 'common_form.html'
    success_url = reverse_lazy('labels:list')
    success_message = _('Label successfully created')

    def get_context_data(self, **kwargs):
        """Return context data for template."""
        context = super().get_context_data(**kwargs)
        context['form_title'] = _('Create label')
        context['form_button'] = _('Create')
        return context


class LabelUpdateView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = Label
    form_class = LabelForm
    template_name = 'common_form.html'
    success_url = reverse_lazy('labels:list')
    success_message = _('Label successfully updated')

    def get_context_data(self, **kwargs):
        """Return context data for template."""
        context = super().get_context_data(**kwargs)
        context['form_title'] = _('Change label')
        context['form_button'] = _('Change')
        return context


class LabelDeleteView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Label
    template_name = 'delete.html'
    success_url = reverse_lazy('labels:list')
    success_message = _('Label successfully deleted')

    def delete(self, request, *args, **kwargs):
        """Override delete method to handle ProtectedError."""
        try:
            self.get_object().delete()
        except ProtectedError:
            messages.error(
                self.request,
                _('It is not possible to delete the label because it is being used'),  # noqa: E501
            )
        else:
            messages.success(
                self.request,
                self.success_message,
            )
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        """Return context data for template."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete label')
        return context
