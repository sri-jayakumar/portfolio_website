# Generated by Django 2.2.5 on 2019-09-07 22:56

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_job_calendar'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description2',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
    ]
