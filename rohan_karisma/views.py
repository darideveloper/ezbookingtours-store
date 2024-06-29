import json
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from rohan_karisma import models


@method_decorator(csrf_exempt, name='dispatch')
class SaleView(View):
    
    def post(self, request):
        
        # Get data
        json_body = json.loads(request.body)
        print(json_body)
        print(json_body["products"].keys())
        transport_type = list(json_body["products"].keys())[0]
        
        # Get product data
        product = json_body["products"][transport_type]
        price = product["price"]
        
        # Get details data
        description = product["description"]
        name = description["name"]
        last_name = description["last_name"]
        email = description["email"]
        passengers = description["passengers"]
        transport_vehicle = description["transport_vehicle"]
        
        # Get arriving and departing data
        arriving = ""
        departing = ""
        for details_key, details_value in description.items():
            if "arriving" in details_key:
                key_clean = details_key.replace("arriving ", "")
                arriving += f"{key_clean}: {details_value}\n"
            elif "departing" in details_key:
                key_clean = details_key.replace("departing ", "")
                departing += f"{key_clean}: {details_value}\n"
                
        # Save model
        sale = models.Sale.objects.create(
            transport_type=transport_type,
            name=name,
            last_name=last_name,
            email=email,
            passengers=passengers,
            price=price,
            # arriving=arriving,
            departing=departing,
            transport_vehicule=transport_vehicle,
        )
        
        return JsonResponse({
            "status": "success",
            "message": f"Sale saved {json_body}"
        })