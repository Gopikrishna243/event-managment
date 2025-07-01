from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=20)
    mobile = models.IntegerField()

class EventDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    area = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    event_city = models.CharField(max_length=100)
    guest_count = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)




        

def __str__(self):
    return self.name
def __str__(self):
    return self.name

    
