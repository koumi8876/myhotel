from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name','email','check_in_date','check_out_date','room','special_request']
        