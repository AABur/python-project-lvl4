import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from task_manager.statuses.models import Status

TEMPLATE = '''
    <a href="{% url 'status-update' record.pk %}">Edit</a>
    <br>
    <a href="{% url 'status-delete' record.pk %}">Delete</a>
'''


class StatusesListTable(tables.Table):

    control_field = tables.TemplateColumn(
        TEMPLATE,
        empty_values=(),
        verbose_name=''
    )

    date_created = tables.DateTimeColumn(
        accessor='date_joined',
        verbose_name=_('Creation date')
    )

    class Meta:
        model = Status
        orderable = False
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', "name", 'date_created')
        attrs = {
            'class': 'table table-striped',
            'id': 'userTable'
        }
