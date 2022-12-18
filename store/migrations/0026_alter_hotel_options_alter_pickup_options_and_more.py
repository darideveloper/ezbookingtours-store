# Generated by Django 4.0.4 on 2022-12-17 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_alter_tour_options_tour_unique_name_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotel',
            options={'verbose_name': 'Hotel', 'verbose_name_plural': 'Hoteles'},
        ),
        migrations.AlterModelOptions(
            name='pickup',
            options={'verbose_name': 'Pick up en hotel', 'verbose_name_plural': 'Pick ups en hoteles'},
        ),
        migrations.AlterModelOptions(
            name='sale',
            options={'verbose_name': 'Venta', 'verbose_name_plural': 'Ventas'},
        ),
        migrations.AlterModelOptions(
            name='tourtime',
            options={'verbose_name': 'Tiempo de tour', 'verbose_name_plural': 'Tiempo de tours'},
        ),
        migrations.RemoveConstraint(
            model_name='tour',
            name='unique_name_location',
        ),
        migrations.AddConstraint(
            model_name='hotel',
            constraint=models.UniqueConstraint(fields=('name', 'address'), name='unique_hotel'),
        ),
        migrations.AddConstraint(
            model_name='pickup',
            constraint=models.UniqueConstraint(fields=('hotel_id', 'tour_time_id', 'time'), name='unique_pick_up'),
        ),
        migrations.AddConstraint(
            model_name='tour',
            constraint=models.UniqueConstraint(fields=('name', 'location'), name='unique_tour'),
        ),
        migrations.AddConstraint(
            model_name='tourtime',
            constraint=models.UniqueConstraint(fields=('tour_id', 'time_start'), name='unique_tour_time'),
        ),
    ]