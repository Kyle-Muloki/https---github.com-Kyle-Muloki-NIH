from django.db import models

# Create your models here.
# models.py
from django.db import models

class Ticket(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    ticket_type = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.ticket_type}'
