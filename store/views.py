from . import models
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
def index (request):
    """ Redirect to store admin page """
    response = {
        "status": "running",
    }
    return JsonResponse(response)

def widget (request, location, tour):
    """ Redirect to store admin page """
    
    # Get tours
    tours = models.Tour.objects.filter (location=location, name=tour, is_active=True)
    
    # Return error of tour not found
    if tours.count() == 0:
        return render(request, 'store/404.html')
    
    # Get tour data
    id = tours[0].id
    adults_price = tours[0].adults_price
    childs_price = tours[0].childs_price
    min_people = tours[0].min_people
    duration = tours[0].duration    
    date_start = tours[0].date_start
    date_end = tours[0].date_end
    monday = tours[0].monday
    tuesday = tours[0].tuesday
    wednesday = tours[0].wednesday
    thursday = tours[0].thursday
    friday = tours[0].friday
    saturday = tours[0].saturday
    sunday = tours[0].sunday
    
    # Render form in get
    if request.method == 'GET':
        
        # Fix start date
        if  date_start < datetime.now().date():
            date_start = datetime.now()    
        
        # # TODO: Validate availability of the tour by dates
        
        # Get tour times
        tour_times = models.TourTime.objects.filter (tour_id=id)
        tour_times_ids = map(lambda tour_time: tour_time.id, tour_times)
        times = list(map(lambda tour_time: tour_time.time_start.strftime("%H:%M"), tour_times))
        
        # Return error of times not found
        if not times:
            return render(request, 'store/404.html')
        
        # Get pick ups available for the tours
        pick_ups = models.PickUp.objects.filter (tour_time_id__in=tour_times_ids)
        
        # Get hotels available for the pick ups
        hotels = []
        for pick_up in pick_ups:
            
            # Get pick up data
            id_pick_up = pick_up.id
            pick_up_time = pick_up.time.strftime("%H:%M")
            tour_time = pick_up.tour_time_id.time_start.strftime("%H:%M")
            
            # Get hotel who match with the pick up   
            hotel = pick_up.hotel_id
            hotel_text = hotel.name if not hotel.address else hotel.name + " - " + hotel.address
            
            hotels.append ({"id": id_pick_up, "hotel": hotel_text, "pick_up": pick_up_time, "tour_time": tour_time})
        
        # Render and submit data        
        return render(request, 'store/widget.html', {
            "adults_price": adults_price,
            "childs_price": childs_price,
            "min_people": min_people,
            "duration": duration,
            "date_start": date_start.strftime("%Y-%m-%d"),
            "date_end": date_end.strftime("%Y-%m-%d"),
            "monday": monday,
            "tuesday": tuesday,
            "wednesday": wednesday,
            "thursday": thursday,
            "friday": friday,
            "saturday": saturday,
            "sunday": sunday,
            "times": times,
            "hotels": hotels,        
        })

    # Get and save form data in post
    elif request.method == 'POST':
        # Get form varuables
        id_pick_up = request.POST.get('hotel')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        adults_num = request.POST.get('adults')
        childs_num = request.POST.get('childs')
        tour_date = request.POST.get('date')
        tour_time = request.POST.get('time')
        
        # Calculate total price
        total = (int(adults_num) * adults_price) + (int(childs_num) * childs_price)
        
        # Save new sale
        new_sale = models.Sale (
            id_pick_up = id_pick_up,
            first_name = first_name,
            last_name = last_name,
            email = email,
            adults_num = adults_num,
            childs_num = childs_num,
            total = total,
            tour_date = tour_date,
            tour_time = tour_time,            
        )
        new_sale.save ()
        return HttpResponse("Saved")
        
        
        