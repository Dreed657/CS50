from django.contrib import admin

from .models import *

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    list_display = ("id", "first", "last")
    filter_horizontal = ("flights",)

class AirportAdmin(admin.ModelAdmin):
    list_display = ("id", "city", "code")

# Register your models here.
admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)