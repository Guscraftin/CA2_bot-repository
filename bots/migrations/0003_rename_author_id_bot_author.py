# Generated by Django 4.1.7 on 2023-03-07 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0002_remove_bot_author_bot_author_id_alter_bot_add_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bot',
            old_name='author_id',
            new_name='author',
        ),
    ]