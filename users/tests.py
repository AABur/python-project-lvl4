from django.test import TestCase

import pytest
from .models import TMUser


@pytest.mark.django_db
def test_user_create():
    user = TMUser.objects.create(
        first_name="John",
        last_name="Doe",
        username="john@gmail.com",
    )
    assert user.full_name() == "John Doe"
