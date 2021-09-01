from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('<int:user_id>/nickname/', views.nickname, name='nickname'),
    path('<int:user_id>/full_name/', views.full_name, name='full_name'),
]
