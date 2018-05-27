from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
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
    name = models.CharField(max_length = 100,null = True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete = models.CASCADE,blank = True)
    location = models.CharField(max_length = 100,null = True)
    avatar = models.ImageField(upload_to = 'avatar/',null = True)  
    def __str__(self):
       return self.name

    @receiver(post_save, sender=User)
    def update_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile(cls):
        profile=UserProfile.objects.all()
        return profile
class Business(models.Model):
    '''
    model that displays the business in an area 
    '''
    name = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete = models.CASCADE)
    email= models.CharField(max_length = 100)

class Post(models.Model):
   '''
   model that saves posts for the neighborhood 
   '''
   title = models.CharField(max_length  = 100,null = True)
   post = models.TextField(max_length=100,null = True)
   profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null = True)
   user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
   time = models.DateTimeField(auto_now_add=True,blank = True,null = True)

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