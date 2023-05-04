from django.db import models

class AirbnbMunicipality (models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True, db_index=True, help_text='Nombre del municipio', default='')
    extra_price = models.FloatField(verbose_name='Precio extra', help_text='Precio extra por el servicio en este municipio', default=0.0)
    
    def __str__ (self):
        return f"{self.name} ({self.extra_price})"
    
    class Meta:
        verbose_name_plural = "AirbnbMunicipalities"
        verbose_name = "AirbnbMunicipality"
    
class Hotel (models.Model): 
    name = models.CharField(max_length=150, verbose_name='Nombre', db_index=True, help_text='Nombre del hotel', default='')
    
    def __str__ (self):
        return f"{self.name}"

class Transport (models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', db_index=True, help_text='Nombre del transporte', default='')
    price = models.FloatField(verbose_name='Precio', help_text='Precio del transporte', default=0.0)
    por_defecto = models.BooleanField(verbose_name='Por defecto', help_text='Transporte por defecto', default=False)
    
    def __str__ (self):
        if self.por_defecto:
            return f"{self.name} ({self.price}) (Por defecto)"
        return f"{self.name} ({self.price})"