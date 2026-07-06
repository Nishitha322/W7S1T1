from django.http import HttpResponse

def index(request):
    return HttpResponse("This is Employee")

# Create your views here.
