# Generated by Django 2.2.4 on 2019-10-11 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='route_name',
        ),
    ]
