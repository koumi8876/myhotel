from django.db import models

# Create your models here.
class Room(models.Model):
 
    roomType = models.CharField(max_length=100,default="single Room")
    roomNumber = models.IntegerField(default="101",unique=True)
    roomDescription = models.TextField(default="Room description")
    roomImage = models.ImageField(upload_to='img/')
    ROOM_STATUS_CHOICES = [
        ("Not Available", 'Not Available'),
        ("Available", 'Available'),
    ]

    roomStatus = models.CharField(max_length=20, choices=ROOM_STATUS_CHOICES, default='Available')
    # roomStatus = models.IntegerField(default=1)
    roomPrice = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.room_number
    # def availability(self):
    #     if(self.roomStatus == 1):
    #         return "Available"
    #     else:
    #         return "Not Available"
        
 