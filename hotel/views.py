# from django.shortcuts import redirect, render,get_object_or_404

# from  .forms import HotelForm
# from  .models import Hotel
# # Create your views here.
# def hotel_view(request):
#    template_name= 'hotel_list.html'
#    context = {
#       "hotel_list": Hotel.objects.all(),
#    }
#    return render(request,template_name,context)

# def createHotel(request):
#     template_name = 'hotel_create.html'
#     form = HotelForm
#     context = {
#         'form':form
#     }
#     if request.method == 'POST':
#         form  = HotelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('hotel_view')
#     return render(request,template_name,context)
   

# def delete_hotel(request,id): 
#    hotel = get_object_or_404(Hotel,id=id)
#    if request.method == 'POST':
#       hotel.delete()
#       return redirect('hotel_view')
#    return render(request,template_name='hotel_list.html')