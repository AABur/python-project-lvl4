from django.urls import path

from task_manager.labels import views

app_name = 'labels'

urlpatterns = [
    path('', views.LabelsListView.as_view(), name='list'),
    path('create/', views.LabelCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.LabelUpdateView.as_view(), name='update'),  # noqa: E501
    path('<int:pk>/delete/', views.LabelDeleteView.as_view(), name='delete'),  # noqa: E501
]
