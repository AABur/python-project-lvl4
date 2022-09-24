"""Tests for the Labels app."""

from http import HTTPStatus

import pytest
from django.urls import reverse

from task_manager.labels.models import Label

LABEL_NAME = 'Label1'


@pytest.mark.usefixtures('logged_in_user')
def test_create_label(client):
    """Test that a user can create a label."""
    response = client.get(reverse('labels:label-create'))
    assert response.status_code == HTTPStatus.OK

    with pytest.raises(Label.DoesNotExist):
        Label.objects.get(name=LABEL_NAME)

    response = client.post(
        reverse('labels:label-create'),
        data={'name': LABEL_NAME},
    )
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('labels:labels')

    label = Label.objects.get(name=LABEL_NAME)
    assert label.name == LABEL_NAME


@pytest.mark.usefixtures('logged_in_user', 'task')
def test_delete_label_assigned_to_task(client, label_used):
    """Test that a user cannot delete a label assigned to a task."""
    response = client.post(
        reverse(
            'labels:label-delete',
            kwargs={'pk': label_used.pk},
        ),
    )
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('labels:labels')
    assert Label.objects.all().count() == 1


@pytest.mark.usefixtures('logged_in_user', 'task')
def test_delete_label_unused(client, label_unused):
    """Test that a user can delete a unused label."""
    label = Label.objects.get(name=label_unused.name)
    assert label.name == label_unused.name

    response = client.post(
        reverse(
            'labels:label-delete',
            kwargs={'pk': label_unused.pk},
        ),
    )
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('labels:labels')

    with pytest.raises(Label.DoesNotExist):
        Label.objects.get(name=label_unused.name)
