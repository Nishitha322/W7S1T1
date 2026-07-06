from django.http import HttpResponse
def index(request):
    return HttpResponse("Available courses")

# Create your views here.
