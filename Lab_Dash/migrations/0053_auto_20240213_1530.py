# Generated by Django 3.1.3 on 2024-02-13 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lab_Dash', '0052_auto_20231128_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sel',
            name='Start_datetime_elli',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 13, 15, 30, 8, 579479), null=True),
        ),
    ]
