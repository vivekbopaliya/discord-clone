# Generated by Django 5.0.3 on 2024-03-12 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_name_user_refresh_token_remove_user_avatar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='refresh_token',
        ),
    ]
