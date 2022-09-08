import pytest

from users.models import TMUser


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """Enable access to the database for all tests."""
    pass


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
