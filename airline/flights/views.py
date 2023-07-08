from django.shortcuts import render

from .models import Flight

# show flights
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    }) 
