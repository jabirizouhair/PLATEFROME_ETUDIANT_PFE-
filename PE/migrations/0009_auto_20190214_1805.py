# Generated by Django 2.1.5 on 2019-02-14 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PE', '0008_actualité'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='etudiant',
        ),
        migrations.RemoveField(
            model_name='note',
            name='matiere',
        ),
        migrations.DeleteModel(
            name='etudiant',
        ),
        migrations.DeleteModel(
            name='matiere',
        ),
        migrations.DeleteModel(
            name='note',
        ),
    ]