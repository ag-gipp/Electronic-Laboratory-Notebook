# Generated by Django 3.1.3 on 2024-02-13 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exp_Main', '0053_auto_20240213_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquid',
            name='Born',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 13, 15, 31, 26, 374738), null=True),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='Death',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 13, 15, 31, 26, 374752), null=True),
        ),
    ]
