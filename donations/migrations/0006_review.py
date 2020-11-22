# Generated by Django 3.1.1 on 2020-11-02 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0005_remove_profile_favorite_orgs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.CharField(max_length=200000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donations.organization')),
            ],
        ),
    ]
