# Generated by Django 3.1.1 on 2020-11-06 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0008_remove_review_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='organization_text',
        ),
    ]
