from django.shortcuts import render,redirect

from booking.form import BookingForm


# Create your views here.

def bookings(request):
    template_name='bookings.html'

    context ={}
    return render(request,template_name,context)


def mybookings(request):
    template_name='mybooking.html'

    context ={}
    return render(request,template_name,context)

def create_bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save(using='hotel')
            # Redirect to a success page or wherever you want to go
            return redirect('success_page')
        # If form is not valid, you might want to handle it, e.g., display errors
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form})