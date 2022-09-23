from http import HTTPStatus

import pytest
from django.urls import reverse

from task_manager.labels.models import Label


@pytest.mark.usefixtures("logged_in_user")
def test_create_label(client):
    assert Label.objects.all().count() == 0

    response = client.get(reverse('labels:label-create'))
    assert response.status_code == HTTPStatus.OK

    with pytest.raises(Label.DoesNotExist):
        Label.objects.get(name='Label1')

    response = client.post(
        reverse('labels:label-create'), data={'name': 'Label1'})

    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('labels:labels')

    label = Label.objects.get(name='Label1')
    assert label.name == 'Label1'


@pytest.mark.usefixtures("logged_in_user")
@pytest.mark.usefixtures("task")
def test_delete_label_assigned_to_task(client, label_used):
    assert Label.objects.all().count() == 1

    response = client.post(
        reverse('labels:label-delete', kwargs={'pk': label_used.pk}))

    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('labels:labels')

    assert Label.objects.all().count() == 1


@pytest.mark.usefixtures("logged_in_user")
@pytest.mark.usefixtures("task")
def test_delete_label_unused(client, label_unused):
    label = Label.objects.get(name=label_unused.name)
    assert label.name == label_unused.name

    response = client.post(
        reverse('labels:label-delete', kwargs={'pk': label_unused.pk}))

    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('labels:labels')

    with pytest.raises(Label.DoesNotExist):
        Label.objects.get(name=label_unused.name)
