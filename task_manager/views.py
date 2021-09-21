from task_manager.forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView


class Home(TemplateView):
    template_name = 'home.html'


class Registration(TemplateView):
    template_name = 'registration.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class Users(TemplateView):
    template_name = 'users.html'
