# Generated by Django 3.2.15 on 2022-08-10 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='executor', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='statuses.status')),
            ],
        ),
    ]
