# Generated by Django 4.0.4 on 2023-07-12 18:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0016_alter_freedays_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freedays',
            name='date',
            field=models.DateField(db_index=True, default=django.utils.timezone.now, help_text='Fecha de día gratis', verbose_name='Fecha'),
        ),
    ]
