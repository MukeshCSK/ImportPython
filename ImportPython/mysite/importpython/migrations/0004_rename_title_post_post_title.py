# Generated by Django 4.0.3 on 2023-04-03 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('importpython', '0003_alter_post_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='post_title',
        ),
    ]
