from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'
    success_message = _('Home')


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'common_form.html'
    success_message = _('Success login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = _('Login')
        context['form_button'] = _('Logon')
        return context


class UserLogoutView(SuccessMessageMixin, LogoutView):
    success_message = _('Success logout')  # FIXME
