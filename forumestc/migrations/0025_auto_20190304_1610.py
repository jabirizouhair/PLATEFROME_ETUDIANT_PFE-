# Generated by Django 2.1.5 on 2019-03-04 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumestc', '0024_auto_20190225_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='active',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='img',
            field=models.ImageField(default='can1.jpg', upload_to=''),
        ),
    ]
