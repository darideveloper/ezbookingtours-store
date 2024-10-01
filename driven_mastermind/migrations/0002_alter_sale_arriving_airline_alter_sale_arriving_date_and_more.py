# Generated by Django 4.2.7 on 2024-10-01 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driven_mastermind', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='arriving_airline',
            field=models.CharField(blank=True, null=True, verbose_name='Aerolínea de llegada'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='arriving_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de llegada'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='arriving_flight',
            field=models.CharField(blank=True, null=True, verbose_name='Vuelo de llegada'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='arriving_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora de llegada'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='departing_airline',
            field=models.CharField(blank=True, null=True, verbose_name='Aerolínea de salida'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='departing_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de salida'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='departing_flight',
            field=models.CharField(blank=True, null=True, verbose_name='Vuelo de salida'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='departing_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora de salida'),
        ),
    ]