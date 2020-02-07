from django import forms
from .models import RestaurantModel,HotelModel,EventModel

class EventForm(forms.ModelForm):
    class Meta:
        model=EventModel
        fields='__all__'

class RestaurantForm(forms.ModelForm):
    class Meta:
        model=RestaurantModel
        fields='__all__'

class HotelForm(forms.ModelForm):
    class Meta:
        model=HotelModel
        fields='__all__'