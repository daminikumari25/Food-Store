from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CONTACT(models.Model):
    name = models.CharField(max_length=122)
    email=models.EmailField(max_length=122)
    subject= models.CharField(max_length=122)
    message= models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class PRODUCT(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image= models.ImageField(upload_to="static/images",default="")

class PRODUCT_DETAILS(models.Model):
    status_choices = [
        ('A', 'EXTRA A'),
        ('B', 'EXTRA B'),
        ('C', 'EXTRA C'),
    ]
    quantity = models.IntegerField()
    extra = models.CharField(max_length=3, choices=status_choices) 

