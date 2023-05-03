# Generated by Django 4.0.3 on 2023-04-03 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importpython', '0007_rename_post_slug_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='post_slug'),
        ),
    ]
