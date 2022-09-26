import django_tables2 as tables

from task_manager.statuses.models import Status

TEMPLATE = """
{% load i18n %}
<a href="{% url 'statuses:status-update' record.pk %}">{% trans 'Update' %}</a>
<br>
<a href="{% url 'statuses:status-delete' record.pk %}">{% trans 'Delete' %}</a>
"""


class StatusesListTable(tables.Table):

    control_field = tables.TemplateColumn(
        TEMPLATE,
        empty_values=(),
        verbose_name='',
    )

    class Meta:
        model = Status
        orderable = False
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('id', 'name', 'date_created')
        attrs = {'class': 'table table-striped'}
