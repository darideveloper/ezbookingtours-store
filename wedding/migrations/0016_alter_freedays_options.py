# Generated by Django 4.0.4 on 2023-07-11 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0015_delete_setting'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='freedays',
            options={'verbose_name': 'Día gratis', 'verbose_name_plural': 'Días gratis'},
        ),
    ]