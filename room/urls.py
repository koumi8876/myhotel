from django.urls import path
from . import views


urlpatterns = [
    path('list-room',views.room_list,name='room_list' ),
    path('create-room', views.room_create, name='room_create'),
    path('room-search', views.search_rooms, name='search_room'),
]