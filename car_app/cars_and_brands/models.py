## cars_and_brands/models.py
from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"ID: {self.id} Brand name: {self.brand_name}"

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    color = models.CharField(max_length=10, default="")
    number_of_seats = models.IntegerField(default=4)

    def __str__(self):
        return f"ID: {self.id} Car brand: {self.brand}"