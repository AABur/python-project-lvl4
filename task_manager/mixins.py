from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect

# TODO 'Вы не авторизованы! Пожалуйста, выполните вход.'
ERROR_MESSAGE_NOT_LOGGED_IN = 'You are not logged in! Please log in.'


class AuthorizationRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = 'login'

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, "ERROR_MESSAGE_NOT_RIGHTS")
            return redirect('users')
        else:
            messages.error(self.request, ERROR_MESSAGE_NOT_LOGGED_IN)
            return redirect(self.login_url)
