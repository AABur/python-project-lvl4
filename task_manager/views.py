from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'


class Users(TemplateView):
    template_name = 'users.html'


class Registration(TemplateView):
    template_name = 'registration.html'
