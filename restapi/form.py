from django import forms
from django.forms import ModelForm
from .models import Airport


class AirportForm(forms.ModelForm):

    class Meta:
        model = Airport
        fields='__all__'
    '''iata= forms.CharField(max_length=100)
    icao= forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    location= forms.CharField(max_length=100)
    gps= forms.CharField(max_length=100)'''