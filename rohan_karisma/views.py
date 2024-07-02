import os
import json
import requests
from dotenv import load_dotenv
from django.views import View
from rohan_karisma import models
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from datetime import datetime
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives


load_dotenv()
STRIPE_FLASK_API = os.getenv("STRIPE_FLASK_API")
HOST = os.getenv("HOST")
ROHAN_KARISMA_PAGE = os.getenv("ROHAN_KARISMA_PAGE")
EMAIL_USER = os.getenv("EMAIL_HOST_USER_OMAR")


@method_decorator(csrf_exempt, name='dispatch')
class SaleView(View):
    """ Get sale json data, save in database and return stripe api response """
    
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
                key_clean = description_key.replace("arriving_", "")
                arriving += f"{key_clean}: {description_value} |\n"
            elif "departing" in description_key:
                key_clean = description_key.replace("departing_", "")
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
    
    
@method_decorator(csrf_exempt, name='dispatch')
class SaleDoneView(View):
    """ Set sale as done and redirect to landing page """
    
    def get(self, request, sale_id):
        
        # Get params
        preview = request.GET.get("preview")
        
        # Get sale
        sale = models.Sale.objects.filter(id=sale_id)
        if not sale.exists():
            return JsonResponse({"message": "Venta no encontrada"}, status=404)
        else:
            sale = sale.first()
        
        # Update sale
        sale.sale_done = True
        sale.save()
        
        # Invoice date
        today = datetime.today().strftime('%Y-%m-%d')
        
        # Invoice details
        details = {}
        arriving_items = sale.arriving.split(" |\n")
        for arriving_item in arriving_items:
            if not arriving_item:
                continue
            key, value = arriving_item.split(": ")
            details[f"Arriving {key.replace('_', '')}"] = value
            
        departing_items = sale.departing.split(" |\n")
        for departing_item in departing_items:
            if not departing_item:
                continue
            key, value = departing_item.split(": ")
            details[f"Departing {key.replace('_', '')}"] = value
            
        details["passengers"] = sale.passengers
        details["transport type"] = sale.transport_type
        details["transport vehicle"] = sale.transport_vehicule
        
        # Render html email template
        context = {
            "today": today,
            "name": sale.name,
            "last_name": sale.last_name,
            "price": f"{sale.price}.00 USD",
            "cta": ROHAN_KARISMA_PAGE,
            "id": sale.id,
            "details": details,
        }
        
        # Send email
        html_message = render_to_string('rohan_karisma/email.html', context)
        plain_message = strip_tags(html_message)
        
        # Send email to client
        emails_subjects = {
            EMAIL_USER: "New Sale in Rohan Karisma",
            sale.email: "Rohan & Karisma Wedding - Transportation Confirmation"
        }
        for to_email, subject in emails_subjects.items():
            print(f"Sending rohan karisma email to {to_email}")
            message = EmailMultiAlternatives(
                subject,
                plain_message,
                EMAIL_USER,
                [to_email]
            )
            message.attach_alternative(html_message, "text/html")
            
            # Not send email in preview
            if not preview:
                message.send()

        if preview:
            # Render done page in preview
            return HttpResponse(html_message)
        else:
            # Redirect to done page
            return redirect(f'{ROHAN_KARISMA_PAGE}?done=true')