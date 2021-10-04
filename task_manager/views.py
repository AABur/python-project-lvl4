from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django_tables2 import SingleTableView

from users.forms import TMUserCreationForm
from users.models import TMUser
from users.tables import UserTable


class HomeView(TemplateView):
    template_name = 'home.html'


class SignUpView(CreateView):
    form_class = TMUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UsersView(SingleTableView):
    template_name = 'users.html'
    model = TMUser
    table_class = UserTable


class UserCreate(CreateView):
    model = TMUser
    fields = ['first_name', 'last_name']


class UserUpdate(UpdateView):
    model = TMUser
    fields = '__all__' # Not recommended (potential security issue if more fields added)


class UserDelete(DeleteView):
    model = TMUser
    success_url = reverse_lazy('users')

class UserDetailView(DetailView):
    """Generic class-based detail view for an author."""
    model = TMUser
