import django_tables2 as tables

from tasks.models import Task

TEMPLATE = '''
    <a href="{% url 'task-update' record.pk %}">Edit</a>
    <br>
    <a href="{% url 'task-delete' record.pk %}">Delete</a>
'''


class TasksListTable(tables.Table):

    control_field = tables.TemplateColumn(
        TEMPLATE,
        empty_values=(),
        verbose_name=''
    )

    name = tables.TemplateColumn(
        '<a href="{% url \'view_task\' record.pk %}">{{ record.name }}</a>'
    )

    class Meta:
        model = Task
        orderable = False
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', 'name', 'status', 'author',
                  'executor', 'create_date', 'links')
        attrs = {'class': 'table table-striped'}
