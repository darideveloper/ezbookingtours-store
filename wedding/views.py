import os
import json
import requests
from dotenv import load_dotenv
from django.http import JsonResponse
from django.views import View
from wedding import models
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Get enviroment variables
load_dotenv()
HOST = os.getenv('HOST')

class IndexView (View):
    
    def get (self, request):
        """ Show confirmation messaje """
        return JsonResponse({
            "status": "success", 
            "message": "Wedding App Running"
        })

@method_decorator(csrf_exempt, name='dispatch')
class ValidateVipCodeView (View):
    
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
        vip_codes_found = models.VipCode.objects.filter(value=vip_code, enabled=True).exists()
        if vip_codes_found:
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
    
    def post (self, request):
        
        # Get data
        json_body = json.loads(request.body)
        
        name = json_body.get("name", "")
        last_name = json_body.get("last-name", "")
        vip_code = json_body.get("vip-code", "")
        stripe_data = json_body.get("stripe-data", {})
        
        if not (name and last_name and vip_code and stripe_data):
            return JsonResponse({
                "status": "error",
                "message": "missing data"
            })            
        
        # Save model
        sale = models.Sale (
            name=name,
            last_name=last_name,
            vip_code=vip_code,
        )
        sale.save ()
        
        # Generate stripe link
        res = requests.post("https://stripe-api-flask.herokuapp.com/", json={
            "user": "cancun_concierge_consolidated_supply",
            "url": f"{HOST}/success/{sale.id}",
            "products": stripe_data
        })
        res_data = res.json()
        
        if not "error" in res_data:
            stripe_link = res_data["stripe_url"]
            return JsonResponse({
                "status": "success",
                "message": "stripe link generated",
                "stripe_link": stripe_link
            })
        else: 
            return JsonResponse({
                "status": "error",
                "message": "error generating stripe link",
                "stripe_link": stripe_link
            })
        