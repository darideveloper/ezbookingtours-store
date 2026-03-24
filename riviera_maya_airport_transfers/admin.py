
from . import models
from django.contrib import admin
from ezbookingtours_store.admin import ModelAdminUnfoldBase

@admin.register (models.AirbnbMunicipality)
class AirbnbMunicipalityAdmin (ModelAdminUnfoldBase):
    list_display = ('name', 'extra_price')
    ordering = ('name',)

@admin.register (models.Hotel)
class HotelAdmin (ModelAdminUnfoldBase):
    list_display = ('name', 'extra_price')
    ordering = ('name',)

@admin.register (models.Transport)
class TransportAdmin (ModelAdminUnfoldBase):
    list_display = ('key', 'name', 'price', 'por_defecto',)
    ordering = ('name',)