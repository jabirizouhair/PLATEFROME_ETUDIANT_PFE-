# Generated by Django 2.1.5 on 2019-02-25 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forumestc', '0023_auto_20190225_1401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='Departement',
            new_name='themedis',
        ),
    ]
