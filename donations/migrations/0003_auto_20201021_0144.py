# Generated by Django 3.1.1 on 2020-10-21 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_auto_20201020_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
