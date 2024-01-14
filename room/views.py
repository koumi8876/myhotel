import json
from django.shortcuts import redirect, render

from room.models import Room
from .forms import RoomForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def room_list(request):
   template_name= 'room_list.html'
   rooms = Room.objects.all()
   context = {
      'list_room':rooms
   }
   return render(request,template_name,context)


def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)  
        if form.is_valid():
            room = form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'room_form.html', {'form': form})



@csrf_exempt  # Use this decorator to exempt CSRF protection for simplicity (consider using csrf tokens in production)
def search_rooms(request):
    if request.method == 'POST':
        data = request.POST  # Assuming the data is sent as form data
        
        # Extract search parameters from the request
        room_type = data.get('room_type')
        room_status = data.get('room_status')
        room_price = data.get('room_price')

        # Build the filter conditions
        filter_conditions = {}
        if room_type:
            filter_conditions['roomType__icontains'] = room_type
        if room_status:
            filter_conditions['roomStatus'] = room_status
        if room_price:
            filter_conditions['roomPrice__lte'] = float(room_price)  # Assuming room_price is a maximum value
        print(room_price)
        # Perform the search
        filter_conditions['roomStatus'] = 'Available'
        rooms = Room.objects.filter(**filter_conditions)
     
        # Serialize the results
        serialized_rooms = [{'roomType': room.roomType, 'roomNumber': room.roomNumber, 'roomStatus': room.roomStatus, 'roomPrice': room.roomPrice} for room in rooms]

        return JsonResponse({'rooms': serialized_rooms})

    return JsonResponse({'message': 'Invalid request method'})