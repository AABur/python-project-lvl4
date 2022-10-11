from django.urls import path

from task_manager.users import views

app_name = 'users'

urlpatterns = [
    path('', views.UsersListView.as_view(), name='list'),
    path('create/', views.SignUpView.as_view(), name='signup'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='update'),  # noqa: E501
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='delete'),  # noqa: E501
]
