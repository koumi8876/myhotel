from django.urls import path
from . import views


urlpatterns = [
    path('',views.bookings,name='Bookings'),
    path('mybookings',views.mybookings,name='mybooking'),
    path('booking-create/',views.mybookings,name='booking_create'),
  
]