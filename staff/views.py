from django.shortcuts import render
from staff.models import Staff
from .form import StaffForm
# Create your views here.
def members(request):
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)  
        if form.is_valid():
            room = form.save()
            # return redirect('room_list')
    else:
        form = StaffForm()
    return render(request, 'room_form.html', {'form': form})