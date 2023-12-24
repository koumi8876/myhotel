from django.shortcuts import render
from room.models import Room
# from hotel.models import Hotel 
# Create your views here.
def home(request):
    template_name = "home.html"
    rooms = Room.objects.all()
    context = {
      'list_room': rooms
    }
    return render(request,template_name,context)
