# Generated by Django 4.0.4 on 2023-07-06 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0005_sale_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=150, unique=True, verbose_name='Nombre del hotel')),
                ('extra_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio extra')),
            ],
            options={
                'verbose_name': 'Hotel',
                'verbose_name_plural': 'Hotel',
            },
        ),
    ]
