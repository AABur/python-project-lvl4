import pytest

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import TMUser


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
    task = Task.objects.create(
        name='Task title',
        description='Task description',
        author=user_author,
        executor=user_executor,
        status=status_used,
    )
    task.labels.add(label_used)
    return task


@pytest.fixture
def logged_in_user(client, user_self):
    """Log in the client with the given user."""
    client.force_login(user_self)
    return user_self
