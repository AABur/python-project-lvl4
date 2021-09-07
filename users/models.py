import datetime

from django.db import models
from django.db.models.fields import IntegerField
from django.utils import timezone

# Create your models here.


class User(models.Model):
    id = models.AutoField(IntegerField, primary_key=True)
    nickname = models.CharField(max_length=10)
    full_name = models.CharField(max_length=30)
    registarration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    def new_uesrs(self):
        return self.registarration_date >= timezone.now() - datetime.timedelta(days=1)
