from django.db import models

class Sale (models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', db_index=True, default='')
    last_name = models.CharField(max_length=150, verbose_name='Apellido', db_index=True, default='')
    sale_datetime = models.DateTimeField(verbose_name='Fecha de venta', db_index=True, default='')
    arriving_price = models.FloatField(verbose_name='Precio de llegada', default=0.0)
    departure_price = models.FloatField(verbose_name='Precio de salida', default=0.0)
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
        
class Settings (models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre del ajuste', db_index=True, default='', unique=True, editable=False)
    value = models.CharField(max_length=150, verbose_name='Valor del ajuste', db_index=True, default='')
    
    def __str__ (self):
        return f"{self.name} - {self.value}"
    
    class Meta:
        verbose_name_plural = "Ajustes"
        verbose_name = "Ajuste"
    