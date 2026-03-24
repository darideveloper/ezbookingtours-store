import os
import json
import requests
from datetime import datetime
from ezbookingtours_store import settings
from dotenv import load_dotenv
from django.http import JsonResponse
from django.views import View
from seema_rohan import models
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from ezbookingtours_store import tools

# Get enviroment variables
load_dotenv()
HOST = os.getenv("HOST")


class IndexView(View):
    """Test home view"""

    def get(self, request):
        """Show confirmation messaje"""
        return JsonResponse({"status": "success", "message": "Seema Rohan App Running"})


@method_decorator(csrf_exempt, name="dispatch")
class BuyView(View):
    """Save sale data and redirect to success page"""

    def post(self, request):

        # Get data
        json_body = json.loads(request.body)
        from_host = json_body.get("from-host", "")

        # Clean from host
        from_host_end = from_host.rfind("/")
        from_host = from_host[:from_host_end]

        # Use the new model method for parsing
        sale, details_objs = models.Sale.from_payload(json_body)

        if not (sale.name and sale.last_name and sale.stripe_data and from_host and sale.phone and sale.email):
            return JsonResponse(
                {
                    "status": "error",
                    "message": "missing data",
                }
            )

        sale.save()
        success_url = f"{HOST}/seema-rohan/success/{sale.id}?from={from_host}"

        # Submit confirmation email
        current_folder = os.path.dirname(os.path.abspath(__file__))
        template_path = os.path.join(
            current_folder, "templates", "seema_rohan", "mail.html"
        )
        tools.send_sucess_mail(
            [
                "Seema Rohan Airport Transfer",
                f"(#{sale.id}) Seema Rohan Airport Transfer",
            ],
            template_path,
            sale.id,
            sale.name,
            sale.last_name,
            sale.total_price,
            details_objs,
            email=sale.email,
        )

        return JsonResponse(
            {"status": "success", "message": "sale saved", "redirect": success_url}
        )


class TransportsView(View):
    """Get available transports"""

    def get(self, request):

        data = models.Transport.objects.all().order_by("id")

        if data:

            return JsonResponse(
                {
                    "status": "success",
                    "message": "transports found",
                    "data": list(data.values()),
                },
                safe=False,
            )

        else:

            return JsonResponse(
                {"status": "error", "message": "transports not found", "data": []},
                safe=False,
            )


class HotelsView(View):
    """Get available hotels"""

    def get(self, request):

        data = models.Hotel.objects.all().order_by("name")

        if data:

            return JsonResponse(
                {
                    "status": "success",
                    "message": "hotels found",
                    "data": list(data.values()),
                },
                safe=False,
            )

        else:

            return JsonResponse(
                {"status": "error", "message": "hotels not found", "data": []},
                safe=False,
            )


class SuccessView(View):
    """Complete sale and redirect to success page"""

    def get(self, request, sale_id):

        # Get from host from get parans
        from_host = request.GET.get("from", "")

        # Query sale from models
        try:
            sale = models.Sale.objects.get(id=sale_id)
        except Exception:
            return redirect(from_host)

        # Complete sale
        sale.is_paid = True
        sale.save()

        # Return success page
        return redirect(f"{from_host}/?thanks=true")
