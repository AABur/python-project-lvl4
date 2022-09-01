import pytest

from users.models import TMUser


@pytest.fixture
def user_self():
    return TMUser.objects.create(
        first_name='John',
        last_name='Doe',
        username='johndoe',
        password='topsecret123',
    )


@pytest.fixture
def user_other():
    return TMUser.objects.create(
        first_name='Guido',
        last_name='Van',
        username='guidovan',
        password='topsecret456',
    )


def test_create_user():
    assert TMUser.objects.all().count() == 0
    user = TMUser.objects.create(
        first_name='John',
        last_name='Doe',
        username='johndoe',
        password='topsecret123',
    )
    assert TMUser.objects.all().count() == 1
    assert user.full_name() == 'John Doe'
