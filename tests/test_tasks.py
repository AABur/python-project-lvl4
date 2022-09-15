from django.urls import reverse
from tasks.models import Task
from http import HTTPStatus

def test_create_task(client, user_author, user_executor, status_used, label_used):
    assert Task.objects.count() == 0

    client.force_login(user_author)
    response = client.get(reverse('task-create'))
    assert response.status_code == HTTPStatus.OK

    response = client.post(reverse('task-create'), data={
        'name': 'Task title',
        'description': 'Task description',
        'author': user_author.id,
        'executor': user_executor.id,
        'status': status_used.id,
        'label': label_used.id,
    })
    assert Task.objects.count() == 1
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('tasks')

    task = Task.objects.get(name='Task title')
    assert task.name == 'Task title'
    assert task.description == 'Task description'
    assert task.author == user_author
    assert task.executor == user_executor
    assert task.status == status_used
    assert task.label == label_used
