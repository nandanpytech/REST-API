from email.policy import default
from operator import mod
from re import T
from unicodedata import category
from django.db import models

# Create your models here.
class Items(models.Model):
    firstname=models.CharField(max_length=250)
    ItemImg=models.CharField(max_length=500)
    Itemprice=models.IntegerField()
    Rating=models.DecimalField(max_digits=5,decimal_places=1)
    Category=models.CharField(max_length=250)
    Best=models.BooleanField(default=True)

    def __str__(self):
        return self.firstname