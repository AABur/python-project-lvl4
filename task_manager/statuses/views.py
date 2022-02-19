from django_tables2 import SingleTableView

from task_manager.statuses.models import Status
from task_manager.statuses.tables import StatusesListTable

# Create your views here.


class StatusesListView(SingleTableView):
    template_name = 'statuses/statuses_list.html'
    model = Status
    table_class = StatusesListTable


class StatusCreateView(SingleTableView):
    template_name = 'statuses/statuses_list.html'
    model = Status
    table_class = StatusesListTable


class StatusUpdateView(SingleTableView):
    template_name = 'statuses/statuses_list.html'
    model = Status
    table_class = StatusesListTable


class StaturDeleteView(SingleTableView):
    template_name = 'statuses/statuses_list.html'
    model = Status
    table_class = StatusesListTable
