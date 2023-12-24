from django.db import models

# Create your models here.
class Room(models.Model):
 
    roomName = models.CharField(max_length=50, blank=True)
    roomType = models.CharField(max_length=100,default="1 bed")
    roomNumber = models.IntegerField(default="101")
    roomDescription = models.TextField(default="Room description")
    roomImage = models.ImageField(upload_to='img/')
    roomStatus = models.IntegerField(default=1)
    roomPrice = models.FloatField(default=0.0)
    
    def availability(self):
        if(self.roomStatus == 1):
            return "Available"
        else:
            return "Not Available"
        
 