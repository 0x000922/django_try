from django.db import models
import datetime
# Create your models here.

class Films(models.Model):
    id = models.AutoField(primary_key = True) # an auto)increment feild as a primary key
    name = models.CharField(max_length = 45,null = False)# automaticaly assigns a not null value
    length_min = models.IntegerField(null = False)
'''



'''
class Customers(models.Model):
    #id = models.AutoField(primary_key = True) django automatically assigns id feild as primary key if not specified
    first_name = models.CharField(max_length = 45,null = True)
    last_name = models.CharField(max_length = 45 ,null = False)
    email = models.EmailField(null = False)

class Rooms(models.Model):
    name = models.CharField(max_length = 45,null = False)
    no_seats = models.IntegerField(null = False) 

class Screenings(models.Model):
    film = models.ForeignKey('Films',on_delete = models.CASCADE,)
    room = models.ForeignKey('Rooms',on_delete = models.CASCADE,)
    start_time = models.DateField()


class Seats(models.Model):
    row_id = models.CharField(max_length =1,null = False)
    seat_number = models.IntegerField(null = False)
    room = models.ForeignKey('Rooms',on_delete=models.CASCADE)

class Bookings(models.Model):
    screening = models.ForeignKey('Screenings',on_delete = models.CASCADE,)
    customers = models.ForeignKey('Customers',on_delete = models.CASCADE,)

class Reserved_seat(models.Model):
    booking = models.ForeignKey('Bookings',on_delete = models.CASCADE,)
    seat = models.ForeignKey('Seats',on_delete = models.CASCADE,)
