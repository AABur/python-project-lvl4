from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from task_manager.users.models import TMUser


class TMUserCreationForm(UserCreationForm):

    class Meta:
        model = TMUser
        fields = ('first_name', 'last_name', 'username')


class TMUserChangeForm(UserChangeForm):

    class Meta:
        model = TMUser
        fields = ('username', 'email')
