import os
import json
import requests
from dotenv import load_dotenv
from django.http import JsonResponse
from django.views import View
from wedding import models
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

# Get enviroment variables
load_dotenv()
HOST = os.getenv('HOST')

class IndexView (View):
    """ Test home view """
    
    def get (self, request):
        """ Show confirmation messaje """
        return JsonResponse({
            "status": "success", 
            "message": "Wedding App Running"
        })

@method_decorator(csrf_exempt, name='dispatch')
class ValidateVipCodeView (View):
    """ Get vip code from json post data and check if it is valid """
    
    def post (self, request):
        """ Check if vip code is valid """
        
        # Get vip code from json post data
        vip_code = json.loads(request.body).get("vip-code", "")
        
        if not vip_code:                                                
            return JsonResponse({
                "status": "error",
                "message": "vip-code missing"
            })
        
        # Query models
        vip_code_found = models.VipCode.objects.filter(value=vip_code, enabled=True).exists()
        if vip_code_found:
            return JsonResponse({
                "status": "success",
                "message": "valid vip code"
            })
        else:
            return JsonResponse({
                "status": "error",
                "message": "invalid vip code"
            })
        
@method_decorator(csrf_exempt, name='dispatch')
class BuyView (View):
    """ Save sale data and redirect to success page or stripe payment page """
    
    def post (self, request):
        
        # Get data
        json_body = json.loads(request.body)
        
        name = json_body.get("name", "")
        last_name = json_body.get("last-name", "")
        price = json_body.get("price", 0)
        vip_code = json_body.get("vip-code", "")
        stripe_data = json_body.get("stripe-data", {})
        from_host = json_body.get("from-host", "")
        
        # Clean from host
        from_host_end = from_host.rfind("/")
        from_host = from_host[:from_host_end]
        
        if not (name and last_name and stripe_data and from_host):
            return JsonResponse({
                "status": "error",
                "message": "missing data",
            })            
        
        vip_code_found = models.VipCode.objects.filter(value=vip_code, enabled=True).exists()
                
        # Save model
        sale = models.Sale (
            name=name,
            price=price,
            last_name=last_name,
            vip_code=vip_code if vip_code_found else "",
            stripe_data=stripe_data
        )
        sale.save ()
        success_url = f"{HOST}/wedding/success/{sale.id}?from={from_host}"
        
        # Validate vip code
        
        # Directly return redirect to success page
        if vip_code_found or price == 0:
            return JsonResponse({
                "status": "success",
                "message": "sale saved",
                "redirect": success_url
            })
        
        # Fix local host link
        if HOST == "http://localhost:8000":
            success_url = f"https://www.darideveloper.com/success/{sale.id}"
            
        # Generate stripe link
        res = requests.post("https://stripe-api-flask.herokuapp.com/", json={
            "user": "cancunconcier",
            "url": from_host,
            "url_success": success_url,
            "products": stripe_data
        })
        
        # Catch error if stripe link is not generated
        try:
            res_data = res.json()
        except:
            return JsonResponse({
                "status": "error",
                "message": "error generating stripe link",
                "redirect": None
            })
            
        # Return stripe link
        return JsonResponse({
            "status": "success",
            "message": "stripe link generated",
            "redirect": res_data["stripe_url"]
        })
            

class TransportsView (View):
    """ Get available transports """
    
    def get (self, request):
        
        data = models.Transport.objects.all().order_by("id")
        
        if data:
        
            return JsonResponse({
                "status": "success",
                "message": "transports found",
                "data": list(data.values())
            }, safe=False)
            
        else:
            
            return JsonResponse({
                "status": "error",
                "message": "transports not found",
                "data": []
            }, safe=False)
            
class HotelsView (View):
    """ Get available hotels """
    
    def get (self, request):
        
        data = models.Hotel.objects.all().order_by("name")
        
        if data:
        
            return JsonResponse({
                "status": "success",
                "message": "hotels found",
                "data": list(data.values())
            }, safe=False)
            
        else:
            
            return JsonResponse({
                "status": "error",
                "message": "hotels not found",
                "data": []
            }, safe=False)
            
class FreeDatesView (View):
    """ Get deys without charge """
    
    def get (self, request):
        
        try:
            # Query free dates from models
            arrival_category = models.FreeDaysCategory.objects.get(name="arrival")
            departure_category = models.FreeDaysCategory.objects.get(name="departure")
            arrival_objs = models.FreeDays.objects.filter(category=arrival_category).order_by('date')
            departure_objs = models.FreeDays.objects.filter(category=departure_category).order_by('-date')

            # Format dates
            arrival_dates = [arrival_obj.date for arrival_obj in arrival_objs]
            departure_dates = [departure_obj.date for departure_obj in departure_objs]
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": "error getting free dates",
                "data": {}
            }, safe=False)
            
        # Return free dates
        return JsonResponse({
            "status": "success",
            "message": "free dates found",
            "data": {
                "arrival": arrival_dates,
                "departure": departure_dates,
            }
        }, safe=False)
        
class SuccessView (View):
    """ Complete sale and redirect to success page """
    
    def get (self, request, sale_id):
        
        # Get from host from get parans
        from_host = request.GET.get("from", "")
        
        # Query sale from models
        try:
            sale = models.Sale.objects.get(id=sale_id)
        except:
            return redirect (from_host)
            
        # Complete sale
        sale.is_paid = True
        sale.save()
        
        # Return success page
        return redirect (f"{from_host}?thanks=true")