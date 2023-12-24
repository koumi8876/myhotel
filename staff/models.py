from django.db import models

# Create your models here.

from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.FloatField(default=0.0)
    telephone = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.name
