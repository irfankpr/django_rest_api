# Generated by Django 4.1.5 on 2023-01-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0002_users_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='last_login',
        ),
        migrations.AddField(
            model_name='users',
            name='DOB',
            field=models.DateTimeField(null=True),
        ),
    ]
