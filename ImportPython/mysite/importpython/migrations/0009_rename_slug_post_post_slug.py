# Generated by Django 4.0.3 on 2023-04-03 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('importpython', '0008_alter_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slug',
            new_name='post_slug',
        ),
    ]
