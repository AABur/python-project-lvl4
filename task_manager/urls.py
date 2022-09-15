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
from django.urls.conf import include

from users.views import (
    SignUpView,
    UserDeleteView,
    UsersListView,
    UserUpdateView,
)

from .views import HomeView, UserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns += [
    path('statuses/', include('statuses.urls')),
    path('labels/', include('labels.urls')),
    path('tasks/', include('tasks.urls')),
    path('users/', include('users.urls')),
]

# urlpatterns += [
#     path('users/', UsersListView.as_view(), name='users'),
#     path('users/create/', SignUpView.as_view(), name='signup'),
#     path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
#     path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
# ]
