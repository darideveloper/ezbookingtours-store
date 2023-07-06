from django.db import models
from django.utils import timezone

class Sale (models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', db_index=True, default='')
    last_name = models.CharField(max_length=150, verbose_name='Apellido', db_index=True, default='')
    sale_datetime = models.DateTimeField(verbose_name='Fecha de venta', db_index=True, default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio', default=0)
    vip_code = models.CharField(max_length=150, verbose_name='Código VIP', db_index=True, default='')
    is_paid = models.BooleanField(verbose_name='Pagado', default=False)
    
    def __str__ (self):
        return f"{self.name} {self.last_name} - {self.sale_datetime}"
    
    class Meta:
        verbose_name_plural = "Ventas"
        verbose_name = "Venta"
        
class VipCode (models.Model):
    value = models.CharField(max_length=150, verbose_name='Valor', db_index=True, default='', unique=True)
    enabled = models.BooleanField(verbose_name='Habilitado', default=False)
    
    def __str__ (self):
        return self.value
    
    class Meta:
        verbose_name_plural = "Códigos VIP"
        verbose_name = "Código VIP"
        
class Setting (models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre del ajuste', db_index=True, default='', unique=True, editable=False)
    value = models.CharField(max_length=150, verbose_name='Valor del ajuste', db_index=True, default='')
    
    def __str__ (self):
        return f"{self.name} - {self.value}"
    
    class Meta:
        verbose_name_plural = "Ajustes"
        verbose_name = "Ajuste"

class Hotel (models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre del hotel', db_index=True, default='', unique=True)
    extra_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio extra', default=0)
    
    def __str__ (self):
        return f"{self.name} - {self.extra_price}"
    
    class Meta:
        verbose_name_plural = "Hotel"
        verbose_name = "Hotel"

class Transport (models.Model):
    key = models.CharField(max_length=150, verbose_name='Clave', db_index=True, help_text='Clave del transporte', default='', unique=True)
    name = models.CharField(max_length=150, verbose_name='Nombre', db_index=True, help_text='Nombre del transporte', default='', unique=True)
    price = models.FloatField(verbose_name='Precio', help_text='Precio del transporte', default=0.0)
    por_defecto = models.BooleanField(verbose_name='Por defecto', help_text='Transporte por defecto', default=False)
    
    def __str__ (self):
        if self.por_defecto:
            return f"{self.name} ({self.price}) (Por defecto)"
        return f"{self.name} ({self.price})"