from django.urls import path

from task_manager.statuses import views

app_name = 'statuses'

urlpatterns = [
    path('', views.StatusesListView.as_view(), name='statuses'),
    path('create/', views.StatusCreateView.as_view(), name='status-create'),
    path('<int:pk>/update/', views.StatusUpdateView.as_view(), name='status-update'),  # noqa: E501
    path('<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status-delete'),  # noqa: E501
]
