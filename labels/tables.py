import django_tables2 as tables

from labels.models import Label

TEMPLATE = '''
    <a href="{% url 'labels:label-update' record.pk %}">Change</a>
    <br>
    <a href="{% url 'labels:label-delete' record.pk %}">Delete</a>
'''


class LabelsListTable(tables.Table):

    control_field = tables.TemplateColumn(
        TEMPLATE,
        empty_values=(),
        verbose_name=''
    )

    class Meta:
        model = Label
        orderable = False
        template_name = "django_tables2/bootstrap4.html"
        fields = ('id', "name", 'date_created')
        attrs = {
            'class': 'table table-striped',
            'id': 'userTable'
        }
