import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from task_manager.users.models import TMUser

TEMPLATE = """
{% load i18n %}
<a href="{% url 'users:user-update' record.pk %}">{% trans 'Update' %}</a>
<br>
<a href="{% url 'users:user-delete' record.pk %}">{% trans 'Delete' %}</a>
"""


class UsersListTable(tables.Table):

    control_field = tables.TemplateColumn(
        TEMPLATE,
        empty_values=(),
        verbose_name='',
    )

    full_name = tables.Column(
        accessor='full_name',
        verbose_name=_('Full name'),
    )

    date_created = tables.DateTimeColumn(
        accessor='date_joined',
        verbose_name=_('Creation date'),
    )

    class Meta:
        model = TMUser
        orderable = False
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('id', 'username', 'full_name', 'date_created')
        attrs = {'class': 'table table-striped'}
