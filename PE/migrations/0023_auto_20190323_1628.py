# Generated by Django 2.1.5 on 2019-03-23 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PE', '0022_auto_20190323_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PE.club'),
        ),
    ]