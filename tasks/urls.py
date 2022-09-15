from django.urls import path

from tasks import views

app_name = 'tasks'


urlpatterns = [
    path('', views.TasksListView.as_view(), name='tasks'),
    path('create/', views.TaskCreateView.as_view(), name='task-create'),
    path(
        '<int:pk>/update/',
        views.TaskUpdateView.as_view(),
        name='task-update',
    ),
    path(
        '<int:pk>/delete/',
        views.TaskDeleteView.as_view(),
        name='task-delete',
    ),
    path('<int:pk>/', views.TaskView.as_view(), name='view_task'),
]
