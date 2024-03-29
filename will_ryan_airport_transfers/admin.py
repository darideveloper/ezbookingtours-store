
from . import models
from django.contrib import admin

@admin.register (models.Hotel)
class HotelAdmin (admin.ModelAdmin):
    list_display = ('name', 'extra_price')
    ordering = ('name',)
    
@admin.register (models.Transport)
class TransportAdmin (admin.ModelAdmin):
    list_display = ('key', 'name', 'price', 'por_defecto',)
    ordering = ('name',)
    
@admin.register (models.Sale)
class SaleAdmin (admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'email', 'sale_datetime', 'price', 'full_data',)
    ordering = ('-id', '-sale_datetime', 'name', 'last_name', 'email', 'price')
    list_filter = ('sale_datetime', 'price')
    