from django.contrib import admin

from .models import Flight, Airport, Passenger


# we can also customize the admin interface by creating a class that inherits from admin.ModelAdmin

class FlightAdmin(admin.ModelAdmin):
    # list_display is a tuple because it can't be mutabel.
    # here we are saying show me the id, origin, destination, and duration of each flight.
    list_display = ("id", "origin", "destination", "duration")
class PassengerAdmin(admin.ModelAdmin):
    # filter_horizontal is a tuple because it can't be mutabel.
    # filler horizontal is saying show me a horizontal filter for the flights.
    filter_horizontal = ("flights",)
    # filter_vertical = ("flights",)


# Registering your models here.
''' we are telling django we want to use the builtin to view and edit our models in the admin interface, instead of using 
python or sql commands. '''

# to apply our customizaation we can add the class FlightAdmin as a second argument to register.
admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passenger, PassengerAdmin)

'''
without customizing

admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Passenger)

'''

