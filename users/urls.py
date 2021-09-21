from django.urls import path

from .views import SignUpView, Users

urlpatterns = [
    path('users/create/', SignUpView.as_view(), name='signup'),
    path('users/', Users.as_view(), name='users'),
]
