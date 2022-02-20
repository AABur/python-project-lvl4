from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'
    success_message = "Home"


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = "Success login"


class UserLogoutView(SuccessMessageMixin, LoginView):
    success_message = "Success logout"
    success_url = reverse_lazy('users')
