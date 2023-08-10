from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage, name='home'),
    path('profile/', profile, name="profile"),
    path('drones/', DroneList.as_view(), name="drones"),
    path('drone/<str:pk>', DroneDetails, name="droneFlights"),
    path('flights/', FlightsListView.as_view(), name="flights"),
    path('view-flight/<int:pk>', FlightDetails.as_view(), name='view-flight'),
    path('add-flight/', createFlight, name="add-flights"),
]