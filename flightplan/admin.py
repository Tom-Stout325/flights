from django.contrib import admin
from .models import Drones, Flights, Profiles

@admin.register(Drones)
class DronesAdmin(admin.ModelAdmin):
    list_display = ['model']
    search_fields = ['model']


@admin.register(Flights)        
class FlightsAdmin(admin.ModelAdmin):
    list_display = ('date', 'event', 'flight_time')
    list_filter = ('city', 'date')
        
admin.site.site_header = "FlightPlan by TSP"

admin.site.register(Profiles)