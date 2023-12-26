from django.shortcuts import render,redirect

from booking.models import Booking
from .form import BookingForm


# Create your views here.

def bookings(request):
    template_name='bookings.html'

    context ={}
    return render(request,template_name,context)


def mybookings(request):
    template_name='mybooking.html'

    context ={}
    return render(request,template_name,context)

def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or wherever you want to go
            return redirect('booking_success')
            
        # If form is not valid, you might want to handle it, e.g., display errors
    else:
        form = BookingForm()

    return render(request, 'bookings.html', {'form': form})

# def booking_create(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('booking_success')  # Redirect to a success page
#     else:
#         form = BookingForm()

#     return render(request, 'book_room.html', {'form': form})