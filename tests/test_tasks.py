"""Tests for the Tasks app."""

from http import HTTPStatus

from django.urls import reverse

from task_manager.tasks.models import Task


def test_create_task(client, user_author, user_executor, status_used, label_used):
    """Test that user can create task."""
    client.force_login(user_author)
    response = client.get(reverse('tasks:task-create'))
    assert response.status_code == HTTPStatus.OK

    response = client.post(reverse('tasks:task-create'), data={
        'name': 'Task title',
        'description': 'Task description',
        'author': user_author.id,
        'executor': user_executor.id,
        'status': status_used.id,
        # 'label': label_used.id,
    })
    assert response.status_code == HTTPStatus.OK
    assert response.url == reverse('tasks:tasks')

    task = Task.objects.get(name='Task title')
    assert task.description == 'Task description'
    assert task.author == user_author
    assert task.executor == user_executor
    assert task.status == status_used
    assert task.label == label_used
