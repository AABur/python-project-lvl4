from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, UpdateView
from django_tables2 import SingleTableView

from task_manager.mixins import AuthorizationRequiredMixin

from .forms import LabelForm
from .models import Label
from .tables import LabelsListTable


class LabelsListView(
    AuthorizationRequiredMixin,
    SingleTableView
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
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels:labels')
    success_message = _('Label successfully created')


class LabelUpdateView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels:labels')
    success_message = _('Label successfully updated')


class LabelDeleteView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels:labels')
    success_message = _('Label successfully deleted')

    def delete(self, request, *args, **kwargs):
        try:
            self.get_object().delete()
        except ProtectedError:
            messages.error(
                self.request,
                _('It is not possible to delete the label because it is being used'),
            )
        else:
            messages.success(
                self.request,
                self.success_message,
            )
        return redirect(self.success_url)
