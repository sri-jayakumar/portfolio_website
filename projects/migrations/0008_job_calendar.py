# Generated by Django 2.2.5 on 2019-09-07 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_remove_job_extra'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='calendar',
            field=models.DateField(default='2019-01-01'),
            preserve_default=False,
        ),
    ]
