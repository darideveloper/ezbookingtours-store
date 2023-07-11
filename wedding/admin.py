from django.contrib import admin
from wedding import models

@admin.register (models.Sale)
class SaleAdmin (admin.ModelAdmin):
    list_display = ('name', 'last_name', 'sale_datetime', 'price', 'vip_code', 'is_paid', 'stripe_data')
    ordering = ('sale_datetime', 'name', 'last_name')
    list_filter = ('sale_datetime', 'is_paid', 'vip_code')
    search_fields = ('name', 'last_name', 'vip_code', 'stripe_data')
    list_max_show_all = 50
    
@admin.register (models.VipCode)
class VipCodeAdmin (admin.ModelAdmin):
    list_display = ('value', 'enabled')
    ordering = ('value',)
    list_filter = ('enabled',)
    list_max_show_all = 50
    
@admin.register (models.Hotel)
class HotelAdmin (admin.ModelAdmin): 
    list_display = ('name', 'extra_price')
    ordering = ('name', 'extra_price')
    
@admin.register (models.Transport)
class TransportAdmin (admin.ModelAdmin): 
    list_display = ('key', 'name', 'price', 'by_default')
    ordering = ('key', 'name', 'price', 'by_default')
    
@admin.register (models.FreeDays)
class FreeDaysAdmin (admin.ModelAdmin): 
    list_display = ('date', 'category')
    ordering = ('date', 'category')
    
@admin.register (models.FreeDaysCategory)
class FreeDaysCategoryAdmin (admin.ModelAdmin): 
    list_display = ('name',)
    ordering = ('name',)