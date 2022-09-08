from http import HTTPStatus

import pytest
from django.urls import reverse

from statuses.models import Status


def test_create_status(client):

    assert Status.objects.all().count() == 0

    response = client.get(reverse('statuses:status-create'))
    assert response.status_code == HTTPStatus.FOUND

    with pytest.raises(Status.DoesNotExist):
        Status.objects.get(name='Status1')

    response = client.post(
        reverse('statuses:status-create'), data={'name': 'Status1'})

    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('statuses:statuses')

    status = Status.objects.get(name='Status1')
    assert status.name == 'Status1'
