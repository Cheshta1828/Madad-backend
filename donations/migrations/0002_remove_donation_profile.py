# Generated by Django 4.2.1 on 2023-06-23 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='Profile',
        ),
    ]
