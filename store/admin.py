from django.contrib import admin
from . import models

@admin.register (models.Tour)
class TourAdmin (admin.ModelAdmin):
    list_display = ('name', 'location', 'duration', 'is_active', "date_start", "date_end")
    list_filter = ('min_people', 'location', 'duration', 'is_active', "date_start", "date_end")
    ordering = ('name', 'location', 'duration', 'is_active', "date_start")
    search_fields = ('name', 'location')
    search_help_text = "Busca tours por nombre o localización"
    
@admin.register (models.Hotel)
class HotelAdmin (admin.ModelAdmin):
    list_display = ('name', 'address',)
    list_filter = ('address',)
    ordering = ('name',)
    search_fields = ('name',)
    search_help_text = "Busca hoteles por nombre"

class TimeTourFilter (admin.SimpleListFilter):
    """ Custom filter for pick up admin """
    
    # Custom filter for pick up admin
    title = 'tour'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'tour'

    def lookups(self, request, model_admin):
        """ Options in filters menu """
        
        # Get tours objects
        tours_times = model_admin.model.objects.all ()
        tours = list(map (lambda tour_time: tour_time.tour_id, tours_times))
        tours_text = set(map (lambda tour: (str(tour.id), tour.name + " - " + tour.location), tours))
        
        return tours_text

    def queryset(self, request, queryset):
        """ Filter queryset by tour id """
        
        if self.value():
            return queryset.filter (tour_id__id=self.value())

@admin.register (models.TourTime)
class TourTimeAdmin (admin.ModelAdmin):
    list_display = ('tour_id', 'time_start')
    list_filter = ('time_start', TimeTourFilter)
    ordering = ('tour_id', 'time_start')
    

@admin.register (models.PickUp)
class PickUpAdmin (admin.ModelAdmin):
    list_display = ('hotel_id', 'tour_time_id', 'time')
    list_filter = ('hotel_id',)
    ordering = ('hotel_id', 'tour_time_id')

@admin.register (models.Sale)
class SalesAdmin (admin.ModelAdmin):
    list_display = ('id', 'email', 'tour', 'pick_up_time', 'total', 'is_paid', 'tour_date', 'buy_date')
    list_filter = ('email', 'is_paid', 'tour_date', 'buy_date')
    ordering = ('email', 'tour', 'pick_up_time', 'total', 'is_paid', 'tour_date', 'buy_date')