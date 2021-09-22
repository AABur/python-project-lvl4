from users.tables import UserTable
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from task_manager.forms import SignUpForm

from django_tables2 import SingleTableView


class HomeView(TemplateView):
    template_name = 'home.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UsersView(SingleTableView):
    template_name = 'users.html'
    model = User
    table_class = UserTable
