# Generated by Django 2.2.5 on 2019-09-07 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_job_description2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='description2',
        ),
    ]
