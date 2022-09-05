from http import HTTPStatus

import pytest
from django.urls import reverse

from users.models import TMUser

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize('url', ['/tasks/', '/labels/', '/statuses/'])
def test_anon_user_is_redirect(client, url):
    response = client.get(url)
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('login')


def test_signup(client):
    response = client.get(reverse('signup'))
    assert response.status_code == HTTPStatus.OK

    with pytest.raises(TMUser.DoesNotExist):
        TMUser.objects.get(username='johndoe')

    response = client.post(reverse('signup'), data={
        'username': 'johndoe',
        'first_name': 'John',
        'last_name': 'Doe',
        'password1': 'topsecret123',
        'password2': 'topsecret123',
    })
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('login')

    user = TMUser.objects.get(username='johndoe')
    assert user.username == 'johndoe'
    assert user.first_name == 'John'
    assert user.last_name == 'Doe'
    assert user.full_name() == 'John Doe'
    assert user.check_password('topsecret123')


def test_delete_user(client, user_self, user_other):
    assert TMUser.objects.all().count() == 2
    response = client.post(reverse('user-delete', kwargs={'pk': user_other.pk}))
    assert response.url == reverse('login')

    client.login(username=user_other.username, password=user_other.password)
    response = client.post(reverse('user-delete', kwargs={'pk': user_other.pk}))
    assert response.url == reverse('login')
    assert TMUser.objects.get(user_self.id) == 1

    client.login(username=user_other.username, password=user_other.password)
    response = client.post(reverse('user-delete', kwargs={'pk': user_other.pk}))
    assert response.url == reverse('login')


def test_delete_not_logged(client, user_self):
    assert TMUser.objects.all().count() == 1
    response = client.post(reverse('user-delete', kwargs={'pk': user_self.pk}))
    assert response.url == reverse('login')
    assert TMUser.objects.all().count() == 1
    user = TMUser.objects.get(username=user_self.username)
    assert user.full_name() == user_self.full_name()


def test_delete_user_self(client, user_self):
    assert TMUser.objects.all().count() == 1
    client.login(username=user_self.username, password=user_self.password)

    response = client.post(reverse('user-delete', kwargs={'pk': user_self.pk}))
    assert response.url == reverse('login')
    assert TMUser.objects.all().count() == 0


def test_update_user_self(client, user_self):
    assert TMUser.objects.all().count() == 1
    client.login(username=user_self.username, password=user_self.password)
    response = client.post(
        reverse('user-update', kwargs={'pk': user_self.pk}),
        data={
            'last_name': 'UPDATED',
            'password1': 'topsecret123',
            'password2': 'topsecret123',
        }
    )
    assert response.url == reverse('login')
    user = TMUser.objects.get(username=user_self.username)
    assert user.last_name == 'UPDATED'
