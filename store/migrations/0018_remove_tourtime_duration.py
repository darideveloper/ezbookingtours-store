# Generated by Django 4.0.4 on 2022-12-17 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_sale_buy_date_alter_sale_tour_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourtime',
            name='duration',
        ),
    ]
