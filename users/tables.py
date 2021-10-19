import django_tables2 as tables
from django_tables2.utils import A

from users.models import TMUser
from django.utils.safestring import mark_safe
from django.urls import reverse


class UserTable(tables.Table):
    TEMPLATE = '''
        <a href="{% url 'user-update' record.pk %}" class="tbl_icon edit">Edit</a>
        <a href="{% url 'user-delete' record.pk %}" class="tbl_icon delete">Delete</a>
    '''

    control = tables.TemplateColumn(
        TEMPLATE,
        empty_values=(),
        verbose_name=''
    )

    class Meta:
        model = TMUser
        template_name = "django_tables2/bootstrap.html"
        fields = ('id', "username", 'full_name', 'date_joined')
