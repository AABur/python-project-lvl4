from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class UsersPageView(TemplateView):
    template_name = 'users.html'


class LoginPageView(TemplateView):
    template_name = 'login.html'


class RegistrationPageView(TemplateView):
    template_name = 'registration.html'
