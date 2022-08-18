from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'
    success_message = _('Home')


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = _('Success login')


class UserLogoutView(SuccessMessageMixin, LogoutView):
    success_message = _('Success logout')  # FIXME
    # success_url = reverse_lazy('users')
