from django.urls import path

from . import views

app_name = 'labels'

urlpatterns = [
    path('', views.LabelsListView.as_view(), name='labels'),
    path('create/', views.LabelCreateView.as_view(), name='label-create'),
    path('<int:pk>/update/', views.LabelUpdateView.as_view(), name='label-update'),
    path('<int:pk>/delete/', views.LabelDeleteView.as_view(), name='label-delete'),
]