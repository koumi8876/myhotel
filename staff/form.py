from django import forms
from .models import  Staff

class RoomForm(forms.ModelForm):
    
    class Meta:
        model = Staff
        fields = ['name','photo','position']
    