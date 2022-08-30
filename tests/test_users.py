import http

import pytest

from users.models import TMUser

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize('url', ['/tasks/', '/labels/', '/statuses/'])
def test_anon_user_is_redirect(client, url):
    response = client.get(url)

    assert response.status_code == http.HTTPStatus.FOUND
    assert response.url == '/login/'


def test_signup(client):
    response = client.get('/users/create/')
    assert response.status_code == http.HTTPStatus.OK

    with pytest.raises(TMUser.DoesNotExist):
        TMUser.objects.get(username='johndoe')

    response = client.post('/users/create/', data={
        'username': 'johndoe',
        'first_name': 'John',
        'last_name': 'Doe',
        'password1': 'topsecret123',
        'password2': 'topsecret123',
    })
    assert response.status_code == http.HTTPStatus.FOUND
    assert response.url == '/login/'

    user = TMUser.objects.get(username='johndoe')
    assert user.username == 'johndoe'
    assert user.first_name == 'John'
    assert user.last_name == 'Doe'
    assert user.full_name() == 'John Doe'
    assert user.check_password('topsecret123')


def test_create_user():
    assert TMUser.objects.all().count() == 0
    user = TMUser.objects.create(
        first_name="John",
        last_name="Doe",
        username="john@gmail.com"
    )
    assert TMUser.objects.all().count() == 1
    assert user.full_name() == "John Doe"


def test_delete_user():
    user1 = TMUser.objects.create(
        first_name="John",
        last_name="Doe",
        username="john@gmail.com"
    )
    user2 = TMUser.objects.create(
        first_name="Jane",
        last_name="Doe",
        username="Jane@gmail.com"
    )


def test_update_user():
    pass
