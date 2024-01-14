from django.shortcuts import render
from room.models import Room
from staff.models import Staff
# from hotel.models import Hotel 
# Create your views here.
def home(request):
    template_name = "home.html"

    # Fetch the first 3 rooms ordered by primary key
    rooms = Room.objects.order_by("pk")[:3]

    # Fetch all staff members
    staff_members = Staff.objects.all()

    context = {
        'list_room': rooms,
        'members': staff_members,
    }

    return render(request, template_name, context)
