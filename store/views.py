from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from . import models

# Create your views here.
def index (request):
    """ Redirect to store admin page """
    response = {
        "status": "running",
    }
    return JsonResponse(response)

def widget (request, location, tour):
    """ Redirect to store admin page """
    response = {
        "status": "running",
    }
    
    tour = models.Tour.objects.filter (location=location, name=tour)
    if not tour:
        return render(request, 'store/404.html')
    
    return HttpResponse (tour.name)
    return render(request, 'store/widget.html', {"text": "text"})
