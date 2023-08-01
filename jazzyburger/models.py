from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = CloudinaryField('image')
    count = 1
    cart = False

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    