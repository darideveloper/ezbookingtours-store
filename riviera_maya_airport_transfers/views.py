from . import models
from django.http import HttpResponse, JsonResponse
from django.core import serializers

def index (request):
    """ Redirect to store admin page """
    response = {
        "status": "running",
    }
    return JsonResponse(response)

def airbnb_municipalities (request):
    
    data = models.AirbnbMunicipality.objects.all()
    data_serialized = serializers.serialize("json", data)
    
    return HttpResponse (data_serialized, content_type="application/json") 

def hotels (request):
    
    data = models.Hotel.objects.all()
    data_serialized = serializers.serialize("json", data)
    
    return HttpResponse (data_serialized, content_type="application/json") 
    
def transports (request):
    
    data = models.Transport.objects.all()
    data_serialized = serializers.serialize("json", data)
    
    return HttpResponse (data_serialized, content_type="application/json") 
    