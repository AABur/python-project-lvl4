"""Tests for the Statuses app."""

from http import HTTPStatus

import pytest
from django.urls import reverse

from task_manager.users.models import TMUser


@pytest.mark.parametrize('url', ['/tasks/', '/labels/', '/statuses/'])
def test_anon_user_is_redirect(client, url):
    """Test that anon user is redirected to login page."""
    response = client.get(url)
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('login')


def test_signup(client):
    """Test that a user can sign up."""
    response = client.get(reverse('users:signup'))
    assert response.status_code == HTTPStatus.OK

    with pytest.raises(TMUser.DoesNotExist):
        TMUser.objects.get(username='johndoe')

    response = client.post(reverse('users:signup'), data={
        'username': 'johndoe',
        'first_name': 'John',
        'last_name': 'Doe',
        'password1': 'topsecret123',
        'password2': 'topsecret123',
    })
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('login')

    user = TMUser.objects.get(username='johndoe')
    assert user.full_name() == 'John Doe'
    assert user.check_password('topsecret123')


def test_delete_not_logged_user(client, user_self):
    """Test that not logged user can't delete user."""
    response = client.post(
        reverse(
            'users:user-delete',
            kwargs={'pk': user_self.pk},
        ),
    )
    assert response.url == reverse('login')
    assert TMUser.objects.all().count() == 1

    user = TMUser.objects.get(username=user_self.username)
    assert user.full_name() == user_self.full_name()


def test_delete_user_self(client, user_self):
    """Test that user can delete himself."""
    client.force_login(user_self)

    response = client.get(
        reverse(
            'users:user-delete',
            kwargs={'pk': user_self.pk},
        ),
    )
    assert response.status_code == HTTPStatus.OK

    response = client.post(
        reverse(
            'users:user-delete',
            kwargs={'pk': user_self.pk},
        ),
    )
    assert response.url == reverse('users:users')
    assert TMUser.objects.all().count() == 0


def test_delete_user_other(client, user_self, user_other):
    """Test that user can't delete other user."""
    client.force_login(user_other)

    response = client.get(
        reverse(
            'users:user-delete',
            kwargs={'pk': user_self.pk},
        ),
    )
    assert response.status_code == HTTPStatus.FOUND

    response = client.post(
        reverse(
            'users:user-delete',
            kwargs={'pk': user_self.pk},
        ),
    )
    assert response.url == reverse('users:users')
    assert TMUser.objects.all().count() == 2


def test_update_user_self(client, user_self):
    """Test that user can update himself."""
    client.force_login(user_self)

    response = client.get(
        reverse(
            'users:user-update',
            kwargs={'pk': user_self.pk},
        ),
    )
    assert response.status_code == HTTPStatus.OK

    response = client.post(
        reverse(
            'users:user-update',
            kwargs={'pk': user_self.pk},
        ),
        data={
            'username': 'johndoe',
            'first_name': 'John_UPD',
            'last_name': 'Doe_UPD',
            'password1': 'topsecret123',
            'password2': 'topsecret123',
        },
    )
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('users:users')

    user = TMUser.objects.get(username='johndoe')
    assert user.full_name() == 'John_UPD Doe_UPD'
