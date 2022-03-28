from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userphoto = models.CharField(max_length=500)
    status = models.CharField(max_length=32)
#
# class User(models.Model):
#     username = models.CharField(max_length=32)
#     password= models.CharField(max_length=32)
#     email= models.CharField(max_length=50)
#     firstname = models.CharField(max_length=32)
#     lastname = models.CharField(max_length=32)
#     userphoto = models.CharField(max_length=500)
#     status = models.CharField(max_length=32)




class Home(models.Model):
    owner = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    coverphoto = models.CharField(max_length=500)
    rent = models.CharField(max_length=32)
    beds = models.CharField(max_length=32)
    baths = models.CharField(max_length=32)
    garage = models.CharField(max_length=32)
    description = models.CharField(max_length=1000)



class Photo(models.Model):
    home = models.CharField(max_length=32)
    photos = models.CharField(max_length=500)
