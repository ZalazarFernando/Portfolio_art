# Generated by Django 5.0 on 2023-12-30 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_user_groups_user_is_superuser_user_last_login_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
