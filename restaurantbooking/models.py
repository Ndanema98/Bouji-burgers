from django.db import models

# Create your models here.

class Customer(models.Model):
    email = models.EmailField()
   
class Table(models.Model):
    seats = models.IntegerField()
    min_people = models.IntegerField()
    max_people = models.IntegerField()

class Reservation(models.Model):
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    party = models.ForeignKey('Customer', on_delete=models.CASCADE)
    spot = models.DateField()