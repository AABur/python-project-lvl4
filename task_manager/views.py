from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django_tables2 import SingleTableView
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import TMUserCreationForm
from users.models import TMUser
from users.tables import UserTable


class HomeView(TemplateView):
    template_name = 'home.html'
    success_message = "Home"


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = TMUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    success_message = "User was created successfully"


class UsersView(SingleTableView):
    template_name = 'users.html'
    model = TMUser
    table_class = UserTable


class UserUpdate(UpdateView):
    model = TMUser
    # Not recommended (potential security issue if more fields added)
    fields = '__all__'


class UserDelete(DeleteView):
    model = TMUser
    success_url = reverse_lazy('users')


class UserDetailView(DetailView):
    """Generic class-based detail view for an author."""
    model = TMUser


class UserLogin(SuccessMessageMixin, LoginView):
    success_message = "Success login"
    success_url = reverse_lazy('users')


class UserLogout(SuccessMessageMixin, LoginView):
    success_message = "Success logout"
    success_url = reverse_lazy('users')
