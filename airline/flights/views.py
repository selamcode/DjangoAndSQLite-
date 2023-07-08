from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger

# show flights
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    }) 
# show flight details
def flight(request, flight_id):

    # pk means primary key
    flight = Flight.objects.get(pk=flight_id)
    
    # Passenger.objects.exclude(flights=flight).all() is saying get all passengers that are not on this flight  but are passangers.

    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

# book a flight
def book(request, flight_id):
    # the request is a post request, because the user will be manipulating data in the database by booking a flight.
    if request.method == "POST":
        # flight is the flight that the user is booking, and passenger is the passenger that the user is booking for.
        flight = Flight.objects.get(pk=flight_id)
        # request.POST["pass"] is like a phone book where you can look up the name of a passenger and get their id.
        # object.get() is saying get the passenger with the id that we just looked up.
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))

        # add the passenger to the flight
        passenger.flights.add(flight)

        # redirect the user to the flight page for the flight they just booked.
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))

