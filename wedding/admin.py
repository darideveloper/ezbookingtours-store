from django.contrib import admin
from wedding import models
from ezbookingtours_store.admin import ModelAdminUnfoldBase


@admin.register(models.Sale)
class SaleAdmin(ModelAdminUnfoldBase):
    list_display = (
        "name",
        "last_name",
        "sale_datetime",
        "price",
        "vip_code",
        "is_paid",
        "phone",
        "email",
        "stripe_data",
    )
    ordering = ("-sale_datetime", "name", "last_name")
    list_filter = ("sale_datetime", "is_paid", "vip_code")
    search_fields = ("name", "last_name", "vip_code", "stripe_data", "phone", "email")
    list_max_show_all = 50


@admin.register(models.VipCode)
class VipCodeAdmin(ModelAdminUnfoldBase):
    list_display = ("value", "enabled")
    ordering = ("value",)
    list_filter = ("enabled",)
    list_max_show_all = 50


@admin.register(models.Hotel)
class HotelAdmin(ModelAdminUnfoldBase):
    list_display = ("name", "extra_price")
    ordering = ("name", "extra_price")


@admin.register(models.Transport)
class TransportAdmin(ModelAdminUnfoldBase):
    list_display = ("key", "name", "price", "by_default")
    ordering = ("key", "name", "price", "by_default")


@admin.register(models.FreeDays)
class FreeDaysAdmin(ModelAdminUnfoldBase):
    list_display = ("date", "category")
    ordering = ("date", "category")


@admin.register(models.FreeDaysCategory)
class FreeDaysCategoryAdmin(ModelAdminUnfoldBase):
    list_display = ("name",)
    ordering = ("name",)
