from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count
from .models import Drones, Flights, User
from .forms import FlightForm
from django.views import generic
from .import models


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('profile')
    else:
        messages.success(request, "Username or Password were incorrect")
        return redirect('profile')
        

def logout_view(request):
    logout(request)
    return redirect('home')



def HomePage(request):
    return render(request, 'flightplan/home.html')

class DroneList(generic.ListView):
    template_name = 'flightplan/drones.html'
    context_object_name = 'drones'
    model = Drones
   
    def get_queryset(self):
        return models.Drones.objects.all()
    

@login_required(login_url='login')  
def DroneDetails(request, pk):
    drone_data = Drones.objects.get(id__exact=pk)
    flight_total = Flights.objects.filter(drone_id=pk).aggregate(total=Sum('flight_time') / 60)
    flight_num = Flights.objects.filter(drone_id=pk).aggregate(total=Count('flight_time'))
    flight_data = Flights.objects.filter(drone_id__exact=pk)
    context ={
        'flight_data': flight_data,
        'flight_total': flight_total,
        'drone_data': drone_data,
        'flight_num': flight_num
    }
    return render(request, "flightplan/drone_view.html", context)


class FlightsListView(generic.ListView):
    template_name = 'flightplan/flights_all.html'
    context_object_name = 'flights'
    model = Flights
    paginate_by = 10
    
    def get_queryset(self):
        return models.Flights.objects.all()
        

class FlightDetails(generic.DetailView):
    template_name = 'flightplan/flight_view.html'
    model = Flights
    context_object_name = 'flight'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


@login_required(login_url='login')
def createFlight(request):
    context={}
    form = FlightForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('flights')
    context['form'] = form
    return render(request, 'flightplan/flight_add.html', context)


@login_required(login_url='login')
def profile(request):
    pilot = User.objects.all()
    flight_total_time = Flights.objects.all().aggregate(total=Sum('flight_time') / 60)
    flight_total_count = Flights.objects.values("drone").aggregate(flights=Count("drone"))
    flight_data = Flights.objects.all().order_by().values("drone").distinct().annotate(total=Sum('flight_time')/ 60).annotate(flights=Count("drone"))
    context ={
        'flight_total_time': flight_total_time,
        'flight_total_count': flight_total_count,
        'flight_data': flight_data,
        'pilot': pilot,
        
    }
    return render(request, 'flightplan/profile.html', context)




