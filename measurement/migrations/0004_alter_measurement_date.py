# Generated by Django 4.1.3 on 2022-11-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_remove_sensor_measurement_measurement_measurement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]