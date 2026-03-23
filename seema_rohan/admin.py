from django.contrib import admin
from seema_rohan import models


@admin.register(models.Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "last_name",
        "sale_datetime",
        "price",
        "is_paid",
        "phone",
        "email",
        "stripe_data",
    )
    ordering = ("-sale_datetime", "name", "last_name")
    list_filter = ("sale_datetime", "is_paid")
    search_fields = ("name", "last_name", "stripe_data", "phone", "email")
    list_max_show_all = 50


@admin.register(models.Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "extra_price")
    ordering = ("name", "extra_price")


@admin.register(models.Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ("key", "name", "price", "by_default")
    ordering = ("key", "name", "price", "by_default")
