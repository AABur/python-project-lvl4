from django import urls

import pytest
from ..users.models import TMUser


@pytest.mark.django_db
def test_user_create():
    user = TMUser.objects.create(
        first_name="John",
        last_name="Doe",
        username="john@gmail.com",
    )
    assert user.full_name() == "John Doe"


@pytest.mark.django_db
@pytest.mark.parametrize('param', [
    ('home'),
    ('signup'),
    ('users'),
    ('statuses'),
    ('labels'),
    ('tasks'),
    # ('user-detail'),
    # ('user-update'),
    # ('user-delete'),
    ('login'),
    # ('logout'),
])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200
