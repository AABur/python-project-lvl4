import pytest

from users.models import TMUser
from statuses.models import Status
from labels.models import Label
from tasks.models import Task


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


@pytest.fixture
def status_used():
    return Status.objects.create(name='Used')


@pytest.fixture
def status_unused():
    return Status.objects.create(name='Unused')


@pytest.fixture
def label_used():
    return Label.objects.create(name='Used')


@pytest.fixture
def label_unused():
    return Label.objects.create(name='Unused')


@pytest.fixture
def user_author():
    return TMUser.objects.create(
        first_name='Author',
        last_name='Author',
        username='author',
        password='topsecret789',
    )


@pytest.fixture
def user_executor():
    return TMUser.objects.create(
        first_name='Executor',
        last_name='Executor',
        username='executor',
        password='topsecret101',
    )


@pytest.fixture
def task(user_author, user_executor, status_used, label_used):
    return Task.objects.create(
        title='Task title',
        description='Task description',
        author=user_author,
        executor=user_executor,
        status=status_used,
        label=label_used,
    )


@pytest.fixture
def logged_in_client(client, user):
    """Log in the client with the given user."""
    client.force_login(user)
    return client
