# models.py
from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    room = models.IntegerField()
    special_request = models.CharField(max_length=255)
    # Add other fields as needed
