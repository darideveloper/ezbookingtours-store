import os
import json
import requests
from dotenv import load_dotenv
from django.views import View
from rohan_karisma import models
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

load_dotenv()
STRIPE_FLASK_API = os.getenv("STRIPE_FLASK_API")
HOST = os.getenv("HOST")


@method_decorator(csrf_exempt, name='dispatch')
class SaleView(View):
    
    def post(self, request):
        
        # Get data
        json_data = json.loads(request.body)
        transport_type = list(json_data["products"].keys())[0]
        
        # Get product data
        product = json_data["products"][transport_type]
        price = product["price"]
        
        # Get description data
        description = product["description"]
        name = description["name"]
        last_name = description["last_name"]
        email = description["email"]
        passengers = description["passengers"]
        transport_vehicle = description["transport_vehicle"]
        
        # Get arriving and departing data
        arriving = ""
        departing = ""
        for description_key, description_value in description.items():
            if "arriving" in description_key:
                key_clean = description_key.replace("arriving ", "")
                arriving += f"{key_clean}: {description_value} |\n"
            elif "departing" in description_key:
                key_clean = description_key.replace("departing ", "")
                departing += f"{key_clean}: {description_value} |\n"
                
        # Save model
        sale = models.Sale.objects.create(
            transport_type=transport_type,
            name=name,
            last_name=last_name,
            email=email,
            passengers=passengers,
            price=price,
            arriving=arriving,
            departing=departing,
            transport_vehicule=transport_vehicle,
        )
        
        # Create stripe link sending data to api
        json_data["url_success"] = f'{HOST}/rohan-karisma/sale/{sale.id}'
        description_text = ""
        for description_key, description_value in description.items():
            description_text += f"{description_key}: {description_value} | "
        json_data["products"][transport_type]["description"] = description_text
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        res = requests.post(STRIPE_FLASK_API, json=json_data, headers=headers)
        json_res = res.json()
        
        # Return same api response
        return JsonResponse(json_res)