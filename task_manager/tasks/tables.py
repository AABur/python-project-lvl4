import django_tables2 as tables

from task_manager.tasks.models import Task

TEMPLATE = """
{% load i18n %}
<a href="{% url 'tasks:task-update' record.pk %}">{% trans 'Change' %}</a>
<br>
<a href="{% url 'tasks:task-delete' record.pk %}">{% trans 'Delete' %}</a>
"""


class TasksListTable(tables.Table):

    control_field = tables.TemplateColumn(
        TEMPLATE,
        empty_values=(),
        verbose_name='',
    )

    name = tables.TemplateColumn(
        '<a href="{% url \'tasks:view_task\' record.pk %}">{{ record.name }}</a>',  # noqa: E501
    )

    class Meta:
        model = Task
        orderable = False
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('id', 'name', 'status', 'author', 'executor', 'date_created')
        attrs = {'class': 'table table-striped'}
