# Generated by Django 4.0.4 on 2024-06-29 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rohan_karisma', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='airline',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='arriving_date',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='arriving_time',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='departing_date',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='departing_time',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='flight_number',
        ),
        migrations.AddField(
            model_name='sale',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='Correo'),
        ),
        migrations.AddField(
            model_name='sale',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Precio'),
        ),
        migrations.AddField(
            model_name='sale',
            name='sale_done',
            field=models.BooleanField(default=False, verbose_name='Venta realizada'),
        ),
        migrations.AddField(
            model_name='sale',
            name='transport_type',
            field=models.CharField(default='', max_length=150, verbose_name='Tipo de transporte'),
        ),
        migrations.AddField(
            model_name='sale',
            name='transport_vehicule',
            field=models.CharField(default='', max_length=150, verbose_name='Vehiculo de transporte'),
        ),
    ]
