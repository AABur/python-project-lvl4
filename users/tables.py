import django_tables2 as tables
from django_tables2.utils import A

from users.models import TMUser


class UserTable(tables.Table):
    edit = tables.Column(
        linkify=(
            'user-update',
            {'pk': A('pk')}
        ),
        empty_values=(),
        verbose_name=''
    )

    class Meta:
        model = TMUser
        template_name = "django_tables2/bootstrap.html"
        fields = ('id', "username", 'full_name', 'date_joined')

    def render_edit(self):
        return 'Edit'
