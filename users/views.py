from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django_tables2 import SingleTableView

from task_manager.mixins import AuthorizationRequiredMixin
from tasks.models import Task
from users.forms import TMUserCreationForm
from users.models import TMUser
from users.tables import UsersListTable


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = TMUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
    success_message = "User was created successfully"


class UsersListView(SingleTableView):
    template_name = 'users/users_list.html'
    model = TMUser
    table_class = UsersListTable


class UserDeleteView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    DeleteView
):

    template_name = 'users/user_delete.html'
    model = TMUser
    success_url = reverse_lazy('users')
    success_message = "SUCCESS_MESSAGE_DELETE_USER"

    def delete(self, request, *args, **kwargs):
        if Task.objects.filter(author=self.request.user.pk) or Task.objects.filter(executor=self.request.user.pk):
            messages.error(
                self.request,
                "ERROR_MESSAGE_NOT_POSSIBLE_DELETE_USER"
            )
            return redirect(reverse_lazy('users'))
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        obj = self.get_object()
        return obj.pk == self.request.user.pk


class UserUpdateView(
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    UpdateView
):

    template_name = 'users/user_update.html'
    model = TMUser
    form_class = TMUserCreationForm
    success_url = reverse_lazy('users')
    success_message = "SUCCESS_MESSAGE_UPDATE_USER"

    def test_func(self):
        obj = self.get_object()
        return obj.pk == self.request.user.pk
