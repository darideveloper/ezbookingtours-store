# Generated by Django 4.0.4 on 2023-07-09 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0010_sale_stripe_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='stripe_data',
            field=models.JSONField(default=dict, verbose_name='Datos de Stripe'),
        ),
    ]
