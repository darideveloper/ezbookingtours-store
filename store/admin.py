from django.contrib import admin
from . import models

@admin.register (models.Tour)
class TourAdmin (admin.ModelAdmin):
    list_display = ('name', 'location', 'duration', 'is_active', "date_start", "date_end")
    list_filter = ('min_people', 'location', 'duration', 'is_active', "date_start", "date_end")
    ordering = ['name', 'location', 'duration', 'is_active', "date_start"]
    search_fields = ['name', 'location']
    search_help_text = "Busca tours por nombre o localización"
    
@admin.register (models.Hotel)
class HotelAdmin (admin.ModelAdmin):
    list_display = ('name', 'address',)
    list_filter = ('address',)
    ordering = ['name']
    search_fields = ['name']
    search_help_text = "Busca hoteles por nombre"
    
@admin.register (models.TourTime)
class TourTimeAdmin (admin.ModelAdmin):
    list_display = ('tour_id', 'time_start', 'duration')
    list_filter = ('tour_id', 'time_start', 'duration')
    ordering = ['tour_id', 'time_start', 'duration']
    
class PickUpATourFilter (admin.SimpleListFilter):
    """ Custom filter for pick up admin """
    
    # Custom filter for pick up admin
    title = 'pick up tour'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'tour'

    def lookups(self, request, model_admin):
        """ Options in filters menu """
        
        # Get tours objects
        pick_ups = model_admin.model.objects.all ()
        tours_times = list(map (lambda pick_up: pick_up.tour_time_id, pick_ups))
        tours = list(map (lambda tour_time: tour_time.tour_id, tours_times))
        tours_text = set(map (lambda tour: (str(tour.id), tour.name + " - " + tour.location), tours))
        
        return tours_text

    def queryset(self, request, queryset):
        """ Filter queryset by tour id """
        
        if self.value():
            return queryset.filter (tour_time_id__tour_id__id=self.value())
            
@admin.register (models.PickUp)
class PickUpAdmin (admin.ModelAdmin):
    list_display = ('hotel_id', 'tour_time_id', 'time')
    list_filter = ('hotel_id', PickUpATourFilter)
    ordering = ['hotel_id', 'tour_time_id']

# @admin.register (models.Sale)
# class SalesAdmin (admin.ModelAdmin):
#     list_display = ('id', 'id_pick_up', 'first_name', 'last_name', 'email', 'adults_num', 'childs_num', 'total', 'is_paid', 'tour_date', 'buy_date')
#     list_filter = ('email', 'is_paid', 'tour_date', 'buy_date')
#     ordering = ['id_pick_up', 'email', 'total', 'is_paid', 'tour_date', 'buy_date']