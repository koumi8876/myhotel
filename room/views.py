from django.shortcuts import redirect, render

from room.models import Room
from .forms import RoomForm

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


def search_rooms(request):

    template_name= 'search_rooms.html'
    form = RoomForm(request.GET)
    if form.is_valid():
        name_to_filter = form.cleaned_data['roomNumber']
        filtered_rooms = Room.objects.filter(name__icontains=name_to_filter)
        print( filtered_rooms)
    else:
        print('Invalid')
    context = {}
    return render(request,template_name,context)
  
   
