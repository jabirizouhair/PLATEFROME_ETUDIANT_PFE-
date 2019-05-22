# Generated by Django 2.1.5 on 2019-02-10 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PE', '0004_evenement_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='evenement',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PE.club'),
        ),
    ]
