from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index (request):
    """ Redirect to store admin page """
    response = {
        "status": "running",
    }
    return JsonResponse(response)
