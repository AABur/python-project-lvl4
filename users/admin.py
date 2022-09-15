from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import TMUserChangeForm, TMUserCreationForm
from .models import TMUser


class TMUserAdmin(UserAdmin):
    add_form = TMUserCreationForm
    form = TMUserChangeForm
    model = TMUser
    list_display = ['email', 'username', ]


admin.site.register(TMUser, TMUserAdmin)
