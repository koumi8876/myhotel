# models.py
from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    children = models.IntegerField()
    adult = models.IntegerField()
    room = models.IntegerField()
    # Add other fields as needed
