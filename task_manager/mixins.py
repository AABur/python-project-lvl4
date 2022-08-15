from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.shortcuts import redirect


class AuthorizationRequiredMixin(LoginRequiredMixin, AccessMixin):
    login_url = 'login'

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, "ERROR_MESSAGE_NOT_RIGHTS")
            return redirect('users')
        else:
            messages.error(self.request, "ERROR_MESSAGE_NOT_LOGGED")
            return redirect(self.login_url)
