from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_tables2 import SingleTableView

from task_manager.mixins import AuthorizationRequiredMixin
from task_manager.tasks.models import Task
from task_manager.users.forms import TMUserCreationForm
from task_manager.users.models import TMUser
from task_manager.users.tables import UsersListTable

USERS_LIST_URL_NAME = 'users:list'


class SignUpView(
    SuccessMessageMixin,
    CreateView,
):
    form_class = TMUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'common_form.html'
    success_message = _('User successfully registered')

    def get_context_data(self, **kwargs):
        """Return context data for template."""
        context = super().get_context_data(**kwargs)
        context['form_title'] = _('Register user')
        context['form_button'] = _('Register')
        return context


class UsersListView(
    SingleTableView,
):
    template_name = 'users/users_list.html'
    model = TMUser
    table_class = UsersListTable


class UserDeleteView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):

    template_name = 'delete.html'
    model = TMUser
    success_url = reverse_lazy(USERS_LIST_URL_NAME)
    success_message = _('User successfully deleted')

    url_user_not_authorized = USERS_LIST_URL_NAME
    message_user_not_authorized = _(
        'You have no permissions to update another user',
    )

    def delete(self, request, *args, **kwargs):
        """If user is the author/executor of any task, it cannot be deleted."""
        is_user_author = Task.objects.filter(author=self.request.user.pk)
        is_user_executor = Task.objects.filter(executor=self.request.user.pk)
        if (is_user_author or is_user_executor).exists():
            messages.error(
                self.request,
                _('Unable to delete a user because they are in use'),
            )
            return redirect(reverse_lazy(USERS_LIST_URL_NAME))
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def check_authorisation(self):
        """Return true if the user is trying to delete himself."""
        return self.get_object() == self.request.user

    def get_context_data(self, **kwargs):
        """Return context data for template."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete user')
        return context


class UserUpdateView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):

    template_name = 'common_form.html'
    model = TMUser
    form_class = TMUserCreationForm
    success_url = reverse_lazy(USERS_LIST_URL_NAME)
    success_message = _('User successfully updated')

    url_user_not_authorized = USERS_LIST_URL_NAME
    message_user_not_authorized = _(
        'You have no permissions to update another user',
    )

    def check_authorisation(self):
        """Return true if the user is trying to update himself."""
        return self.get_object() == self.request.user

    def get_context_data(self, **kwargs):
        """Return context data for template."""
        context = super().get_context_data(**kwargs)
        context['form_title'] = _('Change user')
        context['form_button'] = _('Change')
        return context
