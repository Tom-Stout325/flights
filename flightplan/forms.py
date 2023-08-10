from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'


class ProfileUpdateForm(UserCreationForm):
    user = forms.CharField()
    profile_image = forms.ImageField()
    license = forms.CharField()
    license_date = forms.DateInput()
    
    class Meta:
        model = Profiles
        fields = "__all__"
        widgets = {'license_date': DateInput()}


class DroneForm(forms.ModelForm):
    class Meta:
        model = Drones
        fields = "__all__"
        widgets = {'purchased': DateInput()}
        
        
class FlightForm(forms.ModelForm):
    class Meta:
        model = Flights
        fields = "__all__"
        widgets = {'date': DateInput()}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
          
            data = {
                'class': 'form-control'
            }
        
            self.fields[str(field)].widget.attrs.update(
                data
            )
        