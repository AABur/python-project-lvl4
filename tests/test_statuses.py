"""Tests for the Statuses app."""

from http import HTTPStatus

import pytest
from django.urls import reverse

from task_manager.statuses.models import Status

STATUS_NAME = 'Status1'


@pytest.mark.usefixtures('logged_in_user')
def test_create_status(client):
    """Test that a user can create a status."""
    response = client.get(reverse('statuses:create'))
    assert response.status_code == HTTPStatus.OK

    with pytest.raises(Status.DoesNotExist):
        Status.objects.get(name=STATUS_NAME)

    response = client.post(
        reverse('statuses:create'),
        data={'name': STATUS_NAME},
    )
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('statuses:list')

    status = Status.objects.get(name=STATUS_NAME)
    assert status.name == STATUS_NAME
