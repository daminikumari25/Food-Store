# Generated by Django 3.2.9 on 2021-12-24 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
    ]
