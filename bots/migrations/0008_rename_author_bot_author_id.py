# Generated by Django 4.1.7 on 2023-03-07 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0007_bot_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bot',
            old_name='author',
            new_name='author_id',
        ),
    ]
