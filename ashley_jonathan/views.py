import os
import json
import requests
from dotenv import load_dotenv
from django.views import View
from ashley_jonathan import models
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from datetime import datetime
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


load_dotenv()
STRIPE_FLASK_API = os.getenv("STRIPE_FLASK_API")
HOST = os.getenv("HOST")
ASHLEY_JONATHAN_PAGE = os.getenv(
    "ASHLEY_JONATHAN_PAGE",
    "https://cancunconcierge.net/ashley-jonathan-airport-transfers",
)
EMAIL_USER = settings.EMAIL_HOST_USER


def send_confirmation_emails(sale, preview=False):
    """Render confirmation email and send to client and admin."""
    today = datetime.today().strftime("%Y-%m-%d")

    details = {}
    if sale.arriving:
        arriving_items = sale.arriving.split(" |\n")
        for arriving_item in arriving_items:
            if not arriving_item or ": " not in arriving_item:
                continue
            key, value = arriving_item.split(": ", 1)
            details[f"Arriving {key.replace('_', ' ')}"] = value

    if sale.departing:
        departing_items = sale.departing.split(" |\n")
        for departing_item in departing_items:
            if not departing_item or ": " not in departing_item:
                continue
            key, value = departing_item.split(": ", 1)
            details[f"Departing {key.replace('_', ' ')}"] = value

    details["passengers"] = sale.passengers
    details["transport type"] = sale.transport_type
    details["transport vehicle"] = sale.transport_vehicule

    price_display = f"{sale.price}.00 USD" if sale.price > 0 else "0.00 USD (Free)"

    context = {
        "today": today,
        "name": sale.name,
        "last_name": sale.last_name,
        "price": price_display,
        "cta": ASHLEY_JONATHAN_PAGE,
        "id": sale.id,
        "details": details,
    }

    html_message = render_to_string("ashley_jonathan/email.html", context)
    plain_message = strip_tags(html_message)

    emails_subjects = {
        EMAIL_USER: "New Sale in Ashley & Jonathan",
        sale.email: "Ashley & Jonathan Wedding - Transportation Confirmation",
    }

    if not preview:
        for to_email, subject in emails_subjects.items():
            if not to_email:
                continue
            print(f"Sending ashley jonathan email to {to_email}")
            message = EmailMultiAlternatives(
                subject, plain_message, EMAIL_USER, [to_email]
            )
            message.attach_alternative(html_message, "text/html")
            try:
                message.send()
            except Exception as e:
                print(f"Error sending email to {to_email}: {e}")

    return html_message


@method_decorator(csrf_exempt, name="dispatch")
class SaleView(View):
    """Handle sale booking submissions for free arrival and paid departure/round-trip."""

    def post(self, request):
        json_data = json.loads(request.body)
        transport_type = list(json_data["products"].keys())[0]

        product = json_data["products"][transport_type]
        price = int(product.get("price", 0))

        description = product.get("description", {})
        name = description.get("name", "")
        last_name = description.get("last_name", "")
        email = description.get("email", "")
        passengers = int(description.get("passengers", 1))
        transport_vehicle = description.get("transport_vehicle", "")

        arriving = ""
        departing = ""
        for description_key, description_value in description.items():
            if "arriving" in description_key:
                key_clean = description_key.replace("arriving_", "")
                arriving += f"{key_clean}: {description_value} |\n"
            elif "departing" in description_key:
                key_clean = description_key.replace("departing_", "")
                departing += f"{key_clean}: {description_value} |\n"

        # Check if booking qualifies for free arrival service
        transport_type_lower = transport_type.lower()
        is_free_arrival = (
            price == 0
            or (
                "depart" not in transport_type_lower
                and "round" not in transport_type_lower
                and ("arrival" in transport_type_lower or "airport - hotel" in transport_type_lower)
            )
        )

        if is_free_arrival:
            # Free arrival service: save sale immediately as completed and bypass Stripe
            sale = models.Sale.objects.create(
                transport_type=transport_type,
                name=name,
                last_name=last_name,
                email=email,
                passengers=passengers,
                price=0,
                arriving=arriving,
                departing=departing,
                transport_vehicule=transport_vehicle,
                sale_done=True,
            )

            # Send confirmation emails immediately
            send_confirmation_emails(sale)

            redirect_url = f"{ASHLEY_JONATHAN_PAGE}?done=true"
            return JsonResponse({"stripe_url": redirect_url, "url": redirect_url, "free": True})

        # Paid departure or round-trip service
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
            sale_done=False,
        )

        json_data["url_success"] = f"{HOST}/ashley-jonathan/sale/{sale.id}"
        description_text = ""
        for description_key, description_value in description.items():
            description_text += f"{description_key}: {description_value} | "
        json_data["products"][transport_type]["description"] = description_text
        # Temporarily use rohan-karisma if ashley-jonathan is passed
        if json_data.get("user") == "ashley-jonathan":
            json_data["user"] = "rohan-karisma"

        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        res = requests.post(STRIPE_FLASK_API, json=json_data, headers=headers)
        try:
            json_res = res.json()
        except Exception:
            return JsonResponse(
                {"error": "Failed to create Stripe checkout session", "details": res.text[:200]},
                status=res.status_code if res.status_code != 200 else 502,
            )

        return JsonResponse(json_res)


@method_decorator(csrf_exempt, name="dispatch")
class SaleDoneView(View):
    """Set sale as done upon Stripe payment completion and redirect to landing page."""

    def get(self, request, sale_id):
        preview = request.GET.get("preview")

        sale = models.Sale.objects.filter(id=sale_id)
        if not sale.exists():
            return JsonResponse({"message": "Venta no encontrada"}, status=404)
        sale = sale.first()

        sale.sale_done = True
        sale.save()

        html_message = send_confirmation_emails(sale, preview=bool(preview))

        if preview:
            return HttpResponse(html_message)
        else:
            return redirect(f"{ASHLEY_JONATHAN_PAGE}?done=true")
