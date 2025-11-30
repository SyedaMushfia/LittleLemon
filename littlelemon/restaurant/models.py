from django.db import models

# Create your models here.
class MenuItem(models.Model):
    # id = models.IntegerField()
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    # id = models.IntegerField()
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()    

    def __str__(self):
        return f"{self.name} - {self.booking_date} {self.number_of_guests}"