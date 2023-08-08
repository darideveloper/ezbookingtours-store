from django.db import models
from django.utils import timezone

class Hotel (models.Model): 
    name = models.CharField(max_length=150, verbose_name='Nombre', db_index=True, help_text='Nombre del hotel', default='', unique=True)
    extra_price = models.FloatField(verbose_name='Precio extra', help_text='Precio extra por el servicio en este hotel', default=0.0)
    
    def __str__ (self):
        return f"{self.name}"

class Transport (models.Model):
    key = models.CharField(max_length=150, verbose_name='Clave', db_index=True, help_text='Clave del transporte', default='', unique=True)
    name = models.CharField(max_length=150, verbose_name='Nombre', db_index=True, help_text='Nombre del transporte', default='', unique=True)
    price = models.FloatField(verbose_name='Precio', help_text='Precio del transporte', default=0.0)
    por_defecto = models.BooleanField(verbose_name='Por defecto', help_text='Transporte por defecto', default=False)
    
    def __str__ (self):
        if self.por_defecto:
            return f"{self.name} ({self.price}) (Por defecto)"
        return f"{self.name} ({self.price})"
    
class Sale (models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', db_index=True, default='')
    last_name = models.CharField(max_length=150, verbose_name='Apellido', db_index=True, default='')
    sale_datetime = models.DateTimeField(verbose_name='Fecha de venta', db_index=True, default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio', default=0)
    full_data = models.JSONField(verbose_name='Datos completos de la venta', default=dict, blank=True, null=True)
    
    def __str__ (self):
        return f"{self.name} {self.last_name} - {self.sale_datetime}"
    
    class Meta:
        verbose_name_plural = "Ventas"
        verbose_name = "Venta"