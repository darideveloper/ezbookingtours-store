from django.contrib import admin
from seema_rohan import models
from ezbookingtours_store.admin import ModelAdminUnfoldBase


@admin.register(models.Sale)
class SaleAdmin(ModelAdminUnfoldBase):
    list_display = (
        "name",
        "last_name",
        "transport_type",
        "hotel",
        "sale_datetime",
        "get_total_price",
        "is_paid",
    )
    ordering = ("-sale_datetime", "name", "last_name")
    list_filter = ("sale_datetime", "is_paid", "transport_type", "hotel")
    search_fields = ("name", "last_name", "hotel_name", "phone", "email", "arriving_flight", "departing_flight")
    list_max_show_all = 50
    
    fieldsets = (
        ('Información del cliente', {
            'fields': ('name', 'last_name', 'email', 'phone', 'passengers')
        }),
        ('Información de transporte', {
            'fields': ('transport_type', 'get_total_price', 'is_paid', 'sale_datetime')
        }),
        ('Información del hotel', {
            'fields': ('hotel', 'hotel_name')
        }),
        ('Información de llegada', {
            'fields': ('arriving_date', 'arriving_time', 'arriving_airline', 'arriving_flight')
        }),
        ('Información de salida', {
            'fields': ('departing_date', 'departing_time', 'departing_airline', 'departing_flight')
        }),
        ('Extra', {
            'fields': ('stripe_data',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('sale_datetime', 'stripe_data', 'get_total_price')

    @admin.display(description="Precio total")
    def get_total_price(self, obj):
        return obj.total_price


@admin.register(models.Hotel)
class HotelAdmin(ModelAdminUnfoldBase):
    list_display = ("name", "extra_price")
    ordering = ("name", "extra_price")


@admin.register(models.Transport)
class TransportAdmin(ModelAdminUnfoldBase):
    list_display = ("key", "name", "price", "by_default")
    ordering = ("key", "name", "price", "by_default")
