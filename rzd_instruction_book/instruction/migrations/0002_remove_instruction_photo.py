# Generated by Django 4.2.6 on 2023-10-23 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instruction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instruction',
            name='photo',
        ),
    ]
