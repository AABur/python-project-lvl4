from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class AuthorizationRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = 'login'

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, self.message_user_not_authorized)
            return redirect(self.url_user_not_authorized)
        else:
            messages.error(
                self.request, _('You are not logged in! Please log in.'))
            return redirect(self.login_url)
