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


def test_delete_user(user_self, user_other):
    assert TMUser.objects.all().count() == 2


def test_update_user():
    pass
