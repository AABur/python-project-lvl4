import django_tables2 as tables

from statuses.models import Status

TEMPLATE = '''
    <a href="{% url 'statuses:status-update' record.pk %}">Change</a>
    <br>
    <a href="{% url 'statuses:status-delete' record.pk %}">Delete</a>
'''


class StatusesListTable(tables.Table):

    control_field = tables.TemplateColumn(
        TEMPLATE,
        empty_values=(),
        verbose_name=''
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
