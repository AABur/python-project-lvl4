"""Tests for the Labels app."""

from http import HTTPStatus

import pytest
from django.urls import reverse

from task_manager.labels.models import Label

LABEL_NAME = 'Label1'


@pytest.mark.usefixtures('logged_in_user')
def test_create_label(client):
    """Test that a user can create a label."""
    response = client.get(reverse('labels:create'))
    assert response.status_code == HTTPStatus.OK

    with pytest.raises(Label.DoesNotExist):
        Label.objects.get(name=LABEL_NAME)

    response = client.post(
        reverse('labels:create'),
        data={'name': LABEL_NAME},
    )
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('labels:list')

    label = Label.objects.get(name=LABEL_NAME)
    assert label.name == LABEL_NAME


@pytest.mark.usefixtures('logged_in_user', 'task')
def test_delete_label_assigned_to_task(client, label_used):
    """Test that a user cannot delete a label assigned to a task."""
    response = client.post(
        reverse(
            'labels:delete',
            kwargs={'pk': label_used.pk},
        ),
    )
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('labels:list')
    assert Label.objects.all().count() == 1


@pytest.mark.usefixtures('logged_in_user', 'task')
def test_delete_label_unused(client, label_unused):
    """Test that a user can delete a unused label."""
    label = Label.objects.get(name=label_unused.name)
    assert label.name == label_unused.name

    response = client.post(
        reverse(
            'labels:delete',
            kwargs={'pk': label_unused.pk},
        ),
    )
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('labels:list')

    with pytest.raises(Label.DoesNotExist):
        Label.objects.get(name=label_unused.name)
