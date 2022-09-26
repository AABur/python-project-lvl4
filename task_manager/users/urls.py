from django.urls import path

from task_manager.users import views

app_name = 'users'

urlpatterns = [
    path('', views.UsersListView.as_view(), name='users'),
    path('create/', views.SignUpView.as_view(), name='signup'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'),  # noqa: E501
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user-delete'),  # noqa: E501
]
