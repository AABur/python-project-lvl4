import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from users.models import TMUser

TEMPLATE = '''
    <a href="{% url 'user-update' record.pk %}">Edit</a>
    <br>
    <a href="{% url 'user-delete' record.pk %}">Delete</a>
'''


class UsersListTable(tables.Table):

    control_field = tables.TemplateColumn(
        TEMPLATE,
        empty_values=(),
        verbose_name=''
    )

    full_name = tables.Column(
        accessor='full_name',
        verbose_name=_('Full name'),
    )

    date_created = tables.DateTimeColumn(
        accessor='date_joined',
        verbose_name=_('Creation date')
    )

    class Meta:
        model = TMUser
        orderable = False
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', "username", 'full_name', 'date_created')
        attrs = {
            'class': 'table table-striped',
            'id': 'userTable'
        }
