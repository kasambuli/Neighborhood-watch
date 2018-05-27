from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    '''
    class for saving neighbourhood data
    '''
    name  = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    occupant_count = models.IntegerField()
    def __str__(self):
        return self.name

class UserProfile(models.Model):
   '''
   class that saves the user data 
   '''
   user = models.ForeignKey(User, on_delete = models.CASCADE)
   neighborhood = models.ForeignKey(Neighborhood, on_delete = models.CASCADE)
   location = models.CharField(max_length = 30)


class Business(models.Model):
    '''
    model that displays the business in an area 
    '''
    name = models.CharField(max_length = 30)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete = models.CASCADE)
    email= models.CharField(max_length = 30)

class Post(models.Model):
   '''
   model that saves posts for the neighborhood 
   '''
   title = models.CharField(max_length  = 20)
   post = models.TextField(max_length=100)
   avatar = models.ImageField(upload_to = 'avatar/')
   user_name = models.CharField(max_length = 30)
   time = models.DateTimeField(auto_now_add=True,blank = True)

class Services(models.Model):
   '''
   model that saves the services data
   '''
   police_station = models.CharField(max_length = 30)
   police_no = models.IntegerField(10)
   police_location = models.CharField(max_length = 30)
   healthcare_centre = models.CharField(max_length = 30)
   healthcare_no = models.IntegerField(10)
   healthcare_location = models.CharField(max_length = 30 ,blank = True)