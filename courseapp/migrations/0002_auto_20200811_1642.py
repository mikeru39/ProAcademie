# Generated by Django 3.1 on 2020-08-11 14:42

import courseapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='course_pk',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='path',
            field=models.FileField(default=1, upload_to=courseapp.models.user_dir_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.CharField(default=10, max_length=30),
            preserve_default=False,
        ),
    ]
