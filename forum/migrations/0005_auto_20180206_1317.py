# Generated by Django 2.0 on 2018-02-06 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20180206_1249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='comment',
            new_name='answer',
        ),
    ]
