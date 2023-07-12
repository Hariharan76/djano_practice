from django.db import models


class Destination(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField()
    description=models.CharField(max_length=300)
    offer=models.BooleanField()
  
    
# Create your models here.