# Generated by Django 4.1.5 on 2023-01-05 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0003_remove_users_last_login_users_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='DOB',
            field=models.DateField(null=True),
        ),
    ]
