import os
import json
from ezbookingtours_store import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from will_ryan_airport_transfers import models
from django.core import serializers
from django.views import View
from django.utils.decorators import method_decorator
from ezbookingtours_store import tools

def __sort_data__ (data:list, reverse:bool=False):
    """ Soprt data serializable by name field

    Args:
        data (list): dictionaries with fields
    """
    
    data = json.loads(data)
    
    # Sort by name
    data_sorted = []
    names = list(map(lambda row: row["fields"]["name"], data))
    names.sort()
    
    # Optional reverse
    if reverse:
        names.reverse()
    
    for name in names:
        current_row = list(filter(lambda row: row["fields"]["name"] == name, data))[0]
        data_sorted.append (current_row)  
        
    return json.dumps(data_sorted)

def index (request):
    """ Sample running page """
    response = {
        "status": "running",
    }
    return JsonResponse(response)

def hotels (request):
    
    # Get data
    data = models.Hotel.objects.all()
    data_serialized = serializers.serialize("json", data)
    
    # Order by name
    data_serialized = __sort_data__ (data_serialized, reverse=True)
        
    return HttpResponse (data_serialized, content_type="application/json") 

def transports (request):
    
    # Get data
    data = models.Transport.objects.all()
    data_serialized = serializers.serialize("json", data)
    
    # Order by name
    data_serialized = __sort_data__ (data_serialized)
    
    return HttpResponse (data_serialized, content_type="application/json") 

@method_decorator(csrf_exempt, name='dispatch')
class SalesView (View):
    """ Save sale data and redirect to success page or stripe payment page """
    
    def post (self, request):
        
        # Get data
        json_body = json.loads(request.body)
        
        name = json_body.get("name", "")
        last_name = json_body.get("last-name", "")
        price = json_body.get("price")
        details = json_body.get("details", "")
        email = json_body.get("email", "")
        
        if not (name and last_name and price and details and email):
            return JsonResponse({
                "status": "error",
                "message": "missing data",
            }, status=400)            
                        
        # Save model
        sale = models.Sale (
            name=name,
            last_name=last_name,
            email=email,
            price=price,
            full_data=details.replace('"', ''),
        )
        sale.save ()
        
        # Generate formated details
        details_lines = details.split(",")
        details_objs = []
        for line in details_lines:
            line_split = line.split(":")
            details_objs.append({
                "name": line_split[0],
                "value": line_split[1],
            })
            
        # Submit emails
        current_folder = os.path.dirname(os.path.abspath(__file__))
        template_path = os.path.join(current_folder, "templates", "will_ryan_airport_transfers", "mail.html")
        tools.send_sucess_mail (
            "Voucher Will Ryan Airport Transfers",
            template_path,
            sale.id,
            sale.name,
            sale.last_name,
            sale.price,
            details_objs,
            settings.EMAIL_HOST_USER_OMAR,
            settings.EMAIL_HOST_OMAR,
            email
        )
            
        # Return stripe link
        return JsonResponse({
            "status": "success",
            "message": "Sale saved",
        })