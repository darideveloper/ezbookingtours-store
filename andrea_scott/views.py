import json
from datetime import datetime

from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from andrea_scott import models


@method_decorator(csrf_exempt, name='dispatch')
class SaleView(View):
    
    def post(self, request):
        
        # Get json data
        data = request.body.decode('utf-8')
        json_data = json.loads(data)
        name = json_data['Name']
        last_name = json_data['Last name']
        email = json_data['Email']
        passengers = json_data['Passengers']
        hotel = json_data['Hotel']
        arriving_date_str = json_data['Arriving date']
        arriving_time_str = json_data['Arriving time']
        arriving_airline = json_data['Arriving airline']
        arriving_flight = json_data['Arriving flight']
        departing_date_str = json_data['Departing date']
        departing_time_str = json_data['Departing time']
        departing_airline = json_data['Departing airline']
        departing_flight = json_data['Departing flight']
        total_price = json_data['Price']
        
        # Convert string
        arriving_date = datetime.strptime(arriving_date_str, '%Y-%m-%d')
        arriving_time = datetime.strptime(arriving_time_str, '%H:%M')
        departing_date = datetime.strptime(departing_date_str, '%Y-%m-%d')
        departing_time = datetime.strptime(departing_time_str, '%H:%M')
        
        # Save instance in database
        models.Sale.objects.create(
            client_email=email,
            client_first_name=name,
            client_last_name=last_name,
            passenger_number=passengers,
            hotel=hotel,
            arriving_date=arriving_date,
            arriving_time=arriving_time,
            arriving_airline=arriving_airline,
            arriving_flight=arriving_flight,
            departing_date=departing_date,
            departing_time=departing_time,
            departing_airline=departing_airline,
            departing_flight=departing_flight,
            total_price=total_price,
        )
        
        return JsonResponse({
            "status": "ok",
            "message": "Sale created successfully",
            "data": [],
        })
        
        
        