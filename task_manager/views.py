from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django_tables2 import SingleTableView

from users.forms import TMUserCreationForm
from users.models import TMUser
from users.tables import UsersListTable


class HomeView(TemplateView):
    template_name = 'home.html'
    success_message = "Home"


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = TMUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
    success_message = "User was created successfully"


class UsersListView(SingleTableView):
    template_name = 'users/users_list.html'
    model = TMUser
    table_class = UsersListTable


class UserUpdateView(UpdateView):
    template_name = 'users/user_update.html'
    model = TMUser
    form_class = TMUserCreationForm


class UserDeleteView(DeleteView):
    template_name = 'users/user_delete.html'
    model = TMUser
    success_url = reverse_lazy('users')


class UserDetailView(DetailView):
    model = TMUser
    success_message = "Success DELETE"


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = "Success login"


class UserLogoutView(SuccessMessageMixin, LoginView):
    success_message = "Success logout"
    success_url = reverse_lazy('users')
