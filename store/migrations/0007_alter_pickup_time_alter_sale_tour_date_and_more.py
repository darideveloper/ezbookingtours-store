# Generated by Django 4.0.4 on 2022-12-16 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_pickup_time_alter_sale_tour_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickup',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 12, 16, 0, 15, 48, 495494), help_text='Hora de recogida del tour', verbose_name='Hora de recogida'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='tour_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 0, 15, 48, 496494), help_text='Fecha del tour', verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='date_end',
            field=models.DateField(default=datetime.datetime(2022, 12, 16, 0, 15, 48, 395495), help_text='Fecha de fin del tour', verbose_name='Fecha de fin'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2022, 12, 16, 0, 15, 48, 395495), help_text='Fecha de inicio del tour', verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='tourtime',
            name='time_start',
            field=models.TimeField(default=datetime.datetime(2022, 12, 16, 0, 15, 48, 495494), help_text='Hora de inicio del tour', verbose_name='Hora de inicio'),
        ),
    ]
