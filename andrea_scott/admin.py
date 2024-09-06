from django.contrib import admin
from andrea_scott import models


@admin.register(models.Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'client_email',
        'client_first_name',
        'client_last_name',
        'passenger_number',
        'hotel',
        'arriving_date',
        'arriving_time',
        'arriving_airline',
        'arriving_flight',
        'departing_date',
        'departing_time',
        'departing_airline',
        'departing_flight',
        'reservation_date_time',
        'total_price',
        'is_paid',
    )
    list_display_links = (
        'id',
        'client_email',
    )
    list_filter = (
        'is_paid',
        'arriving_date',
        'departing_date',
        'reservation_date_time',
    )
    search_fields = (
        'client_first_name',
        'client_last_name',
        'client_eamil',
        'hotel',
        'arriving_airline',
        'arriving_flight',
        'departing_airline',
        'departing_flight',
    )