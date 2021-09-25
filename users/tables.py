import django_tables2 as tables

from users.models import TMUser


class UserTable(tables.Table):
    class Meta:
        model = TMUser
        template_name = "django_tables2/bootstrap.html"
        fields = ('id', "username", 'full_name', 'date_joined')
