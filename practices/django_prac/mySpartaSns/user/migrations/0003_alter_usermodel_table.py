# Generated by Django 4.1.7 on 2023-04-05 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_usermodel_managers_remove_usermodel_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='usermodel',
            table='auth_user',
        ),
    ]
