from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django_tables2 import SingleTableView

from task_manager.mixins import AuthorizationRequiredMixin
from task_manager.tasks.models import Task
from task_manager.users.forms import TMUserCreationForm
from task_manager.users.models import TMUser
from task_manager.users.tables import UsersListTable


class SignUpView(
    SuccessMessageMixin,
    CreateView,
):
    form_class = TMUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
    success_message = _('User successfully registered')


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
    success_url = reverse_lazy('users:users')
    success_message = _('User successfully deleted')

    url_user_not_authorized = 'users:users'
    message_user_not_authorized = _(
        'You have no permissions to update another user.')

    def delete(self, request, *args, **kwargs):
        """If a user is the author or executor of any task, it cannot be deleted."""
        if (
            Task.objects.filter(author=self.request.user.pk) or
            Task.objects.filter(executor=self.request.user.pk)
        ).exists():
            messages.error(
                self.request,
                _('Unable to delete a user because they are in use'),
            )
            return redirect(reverse_lazy('users:users'))
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def check_authorisation(self):
        return self.get_object() == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete user')
        return context


class UserUpdateView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):

    template_name = 'users/user_update.html'
    model = TMUser
    form_class = TMUserCreationForm
    success_url = reverse_lazy('users:users')
    success_message = _('User successfully updated')

    url_user_not_authorized = 'users:users'
    message_user_not_authorized = _(
        'You have no permissions to update another user.')

    def check_authorisation(self):
        return self.get_object() == self.request.user
