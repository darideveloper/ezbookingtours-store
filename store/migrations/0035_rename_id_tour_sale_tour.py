# Generated by Django 4.0.4 on 2022-12-24 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0034_sale_adults_num_sale_buy_date_sale_childs_num_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='id_tour',
            new_name='tour',
        ),
    ]