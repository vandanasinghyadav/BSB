# Generated by Django 5.1.4 on 2025-01-02 17:34

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=200)),
                ('courseFees', models.CharField(max_length=200)),
                ('courseDuration', models.CharField(max_length=200)),
                ('courseDescription', tinymce.models.HTMLField()),
                ('courseImage', models.ImageField(upload_to='course_image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
