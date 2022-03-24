from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    password= models.CharField(max_length=32)
    email= models.CharField(max_length=50)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)




class Home(models.Model):
    owner = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)


class Photo(models.Model):
    home = models.CharField(max_length=32)
    photos = models.CharField(max_length=500)
