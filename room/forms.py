from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['roomType','roomNumber','roomDescription','roomImage','roomStatus','roomPrice']
    

class SearchForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['roomNumber']
        