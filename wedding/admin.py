from django.contrib import admin
from wedding import models

@admin.register (models.Sale)
class SaleAdmin (admin.ModelAdmin):
    list_display = ('name', 'last_name', 'sale_datetime', 'arriving_price', 'departure_price', 'vip_code', 'is_paid')
    ordering = ('sale_datetime', 'name', 'last_name')
    list_filter = ('sale_datetime', 'is_paid', 'vip_code')
    list_max_show_all = 50
    
@admin.register (models.VipCode)
class VipCodeAdmin (admin.ModelAdmin):
    list_display = ('value', 'enabled')
    ordering = ('value',)
    list_filter = ('enabled',)
    list_max_show_all = 50
    
@admin.register (models.Settings)
class SettingsAdmin (admin.ModelAdmin): 
    list_display = ('name', 'value')
    ordering = ('name',)
    list_max_show_all = 50