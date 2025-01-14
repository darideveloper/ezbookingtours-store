import os
import requests
from . import models
from datetime import datetime
from dotenv import load_dotenv
from django.urls import reverse
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .tools import send_sucess_mail

# Get enviroment variables
load_dotenv()
HOST = os.getenv('HOST')

# Create your views here.
def index (request):
    """ Redirect to store admin page """
    response = {
        "status": "running",
    }
    return JsonResponse(response)

@csrf_exempt
def widget (request, location, tour):
    """ Redirect to store admin page """
        
    # Get tours
    tours = models.Tour.objects.filter (location=location, name=tour, is_active=True)
    
    # Return error of tour not found
    if tours.count() == 0:
        return render(request, 'store/widget_404.html')
    
    # Get tour data
    id = tours[0].id
    adults_price = tours[0].adults_price
    childs_price = tours[0].childs_price
    min_people = tours[0].min_people
    duration = tours[0].duration    
    is_active = tours[0].is_active
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
        
        # Validate end date
        if date_end < datetime.now().date():
            return render(request, 'store/widget_404.html') 
        
        # Validate active status
        if not is_active:
            return render(request, 'store/widget_404.html') 
        
        # Fix start date
        if  date_start < datetime.now().date():
            date_start = datetime.now()
        
        # Get tour times
        tour_times = models.TourTime.objects.filter (tour_id=id)
        tour_times_ids = map(lambda tour_time: tour_time.id, tour_times)
        times = list(map(lambda tour_time: tour_time.time_start.strftime("%H:%M"), tour_times))
        
        # Return error of times not found
        if not times:
            return render(request, 'store/widget_404.html')
        
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
            "now": datetime.now().strftime("%Y-%m-%d"),    
        })

    # Process form in post
    elif request.method == 'POST':
        
        # Get form varuables
        id_pick_up = request.POST.get("hotel", "")
        first_name = request.POST.get("first-name", "")
        last_name = request.POST.get("last-name", "")
        email = request.POST.get("email", "")
        adults_num = int(request.POST.get('adults', 0))
        childs_num = int(request.POST.get('childs', 0))
        tour_date = request.POST.get('date', "")
        tour_time = request.POST.get('time', "")
    
        # Get pick object if exists
        pick_up = None
        if id_pick_up: 
            pick_up = models.PickUp.objects.get(id=id_pick_up)
    
        # Calculate total price
        total = (adults_num * adults_price) + (childs_num * childs_price)
        
        # Save new sale
        new_sale = models.Sale (
            hotel = pick_up.hotel_id if pick_up else None,
            pick_up_time = pick_up.time if pick_up else None,
            tour = tours[0],
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

        # Create stripe description
        stripe_description = f"Tour de ezbookingtours.com, en la fecha {tour_date} y hora {tour_time}. "
        if pick_up:
            pickup_time = pick_up.time.strftime("%H:%M")
            hotel = pick_up.hotel_id.name
            stripe_description += f"Pick up en hotel {hotel} a las {pickup_time}"
            
        # Generate data for stripe api
        products = {}
        if adults_num > 0: 
            products[f"{tour} {location}, adulto"] = {
                "amount": adults_num,
                "image_url": "https://ezbookingtours.com/wp-content/uploads/2022/04/EZ-Booking-Tours-Logo.png",
                # "price": float(1),
                "price": float(adults_price),
                "description": stripe_description
            }
            
        if childs_num > 0:
            products[f"{tour} {location}, niño"] = {
                "amount": childs_num,
                "image_url": "https://ezbookingtours.com/wp-content/uploads/2022/04/EZ-Booking-Tours-Logo.png",
                "price": float(childs_price),
                "description": stripe_description
            }
            
        request_json = {
            "user": "cancun_concierge_consolidated_supply",
            "url": f"{HOST}/success/{new_sale.id}",
            "products": products 
        }
        
        # Get buy url from stripe api
        res = requests.post("https://services.darideveloper.com/stripe-api/", json=request_json)
        res_data = res.json()
        if not "error" in res_data:
            stripe_link = res_data["stripe_url"]

            # Return payment page who redirect to stripe 
            return render(request, 'store/payment.html', {"stripe_link": stripe_link})
        else: 
            # Return error page
            return render(request, 'store/widget_404.html')


def success (request, sale_id):
    
    # Get sale with id
    sale = models.Sale.objects.filter(id=sale_id).first()
    
    # Return error page if sale not exists
    if not sale:
        return render(request, 'store/widget_404.html')
    
    # Update pay status
    sale.is_paid = True
    sale.save ()
    
    # Generate admins sale link
    admin_sale_link = f"{HOST}/admin/store/sale/{sale.id}/change/" 
    
    context = {
        "id_sale": sale.id,
        "is_email": False,
        "admin_sale_link": admin_sale_link,
        "tour": {
            "name": sale.tour.name,
            "location": sale.tour.location,
            "hotel": sale.hotel.name if sale.hotel else "",
            "pick_up": sale.pick_up_time.strftime("%H:%M") if sale.pick_up_time else "",
            "adults_num": sale.adults_num,
            "childs_num": sale.childs_num,
            "adults_price": sale.tour.adults_price,
            "childs_price": sale.tour.childs_price,
            "total": sale.total,
            "date": sale.tour_date,
            "time": sale.tour_time, 
        },
        "buyer": {
            "first_name": sale.first_name,
            "last_name": sale.last_name,
            "email": sale.email,  
        }
    }
    
    # Send email to admin
    send_sucess_mail (context)
        
    # Return summary data in template    
    return render(request, 'store/success.html', context)
    
def error_404 (request, exception):
    return render(request, 'store/404.html')

def error_404_view (request):
    return render(request, 'store/404.html')