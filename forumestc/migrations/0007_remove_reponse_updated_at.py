# Generated by Django 2.1.5 on 2019-02-18 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forumestc', '0006_auto_20190218_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reponse',
            name='updated_at',
        ),
    ]
