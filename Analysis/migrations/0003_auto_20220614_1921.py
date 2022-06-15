# Generated by Django 3.1.3 on 2022-06-14 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analysis', '0002_lmpcosolventanalysis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lmpcosolventanalysis',
            name='Anz_EtOH',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lmpcosolventanalysis',
            name='Anz_H2O',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lmpcosolventanalysis',
            name='Height',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
