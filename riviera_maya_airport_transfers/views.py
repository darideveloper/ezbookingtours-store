from django.http import HttpResponse, JsonResponse

def index (request):
    """ Redirect to store admin page """
    response = {
        "status": "running",
    }
    return JsonResponse(response)

def airbnb_municipalities (request):
    
    return HttpResponse ("Hello world") 

def hotels (request):
    
    return HttpResponse ("Hello world") 
    
def transports (request):
    
    return HttpResponse ("Hello world") 
    