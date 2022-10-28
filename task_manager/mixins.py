from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _

USER_NOT_LOGGED_MESSAGE = 'You are not logged in! Please log in.'


class AuthorizationRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = 'login'

    def get_test_func(self):
        """Get test function for authorization."""
        try:
            return self.check_authorisation
        except Exception:
            return self.test_func

    def test_func(self):
        """Check if user is authorized to access the page."""
        return True

    def handle_no_permission(self):
        """Handle no permission."""
        if self.request.user.is_authenticated:
            messages.error(self.request, self.message_user_not_authorized)
            return redirect(self.url_user_not_authorized)
        else:
            messages.error(self.request, _(USER_NOT_LOGGED_MESSAGE))  # noqa: WPS503, E501
            return redirect(self.login_url)
