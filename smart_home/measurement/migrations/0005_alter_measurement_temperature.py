# Generated by Django 4.2.2 on 2023-06-18 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_alter_measurement_sensor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]