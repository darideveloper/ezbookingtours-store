from django.contrib import admin
from rohan_karisma.models import Sale


@admin.register(Sale)
class AdminSale(admin.ModelAdmin):
    
    # Search in all fields
    list_display = [field.name for field in Sale._meta.get_fields()]
    search_fields = [field.name for field in Sale._meta.get_fields()]
    list_filter = [
        'transport_type',
        'passengers',
        'price',
        'transport_vehicule',
        'sale_done',
    ]
    ordering = [field.name for field in Sale._meta.get_fields()]
    list_per_page = 50