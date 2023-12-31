# Generated by Django 4.2.4 on 2023-08-31 09:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_img', models.ImageField(upload_to='')),
                ('post_header', models.CharField(max_length=50)),
                ('post_content', models.CharField(max_length=255)),
                ('post_date', models.DateTimeField(default=datetime.datetime.now)),
                ('post_auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'gallery',
            },
        ),
    ]
