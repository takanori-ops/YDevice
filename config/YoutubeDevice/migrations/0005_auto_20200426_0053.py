# Generated by Django 2.1.2 on 2020-04-25 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('YoutubeDevice', '0004_auto_20200426_0052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='user',
            new_name='edit_user',
        ),
    ]