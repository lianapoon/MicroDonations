# Generated by Django 3.1.1 on 2020-11-12 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0008_auto_20201105_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='organization',
            name='price',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
