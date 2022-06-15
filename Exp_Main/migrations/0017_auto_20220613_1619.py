# Generated by Django 3.1.3 on 2022-06-13 14:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exp_Main', '0016_auto_20220612_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='lmp',
            name='Chem_ETOH',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lmp',
            name='Chem_H2O',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='Born',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 13, 16, 19, 22, 625869), null=True),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='Death',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 13, 16, 19, 22, 625878), null=True),
        ),
    ]
