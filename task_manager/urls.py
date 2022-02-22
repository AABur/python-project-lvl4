"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import TemplateView

from task_manager.statuses.views import (
    StatusDeleteView,
    StatusCreateView,
    StatusesListView,
    StatusChangeView,
)
from users.views import (
    SignUpView,
    UserDeleteView,
    UserDetailView,
    UsersListView,
    UserUpdateView,
)

from .views import HomeView, UserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', TemplateView.as_view(template_name='home.html'), name='labels'),
    path('', TemplateView.as_view(template_name='home.html'), name='tasks'),
]

urlpatterns += [
    path('users/', UsersListView.as_view(), name='users'),
    path('users/create/', SignUpView.as_view(), name='signup'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]

urlpatterns += [
    path('statuses/', StatusesListView.as_view(), name='statuses'),
    path('statuses/create/', StatusCreateView.as_view(), name='status-create'),
    path(
        'statuses/<int:pk>/update/',
        StatusChangeView.as_view(),
        name='status-update',
    ),
    path(
        'statuses/<int:pk>/delete/',
        StatusDeleteView.as_view(),
        name='status-delete',
    ),
]
