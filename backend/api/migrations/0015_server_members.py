# Generated by Django 5.0.3 on 2024-03-16 05:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_server_members_member_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='members',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='server_members', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]