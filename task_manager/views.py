from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from task_manager.forms import SignUpForm


class HomeView(TemplateView):
    template_name = 'home.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UsersView(TemplateView):
    template_name = 'users.html'
