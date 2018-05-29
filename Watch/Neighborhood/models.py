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
    def save_neighborhood(self):
        self.save()

    @classmethod
    def delete_neighborhood(cls,id):
        cls.objects.filter(id).delete()
    @classmethod
    def update_neighborhood(cls,id,new_name):
        cls.objects.filter(id=id).update(name = new_name)

    @classmethod
    def update_occupant_count(cls,id,new_occupant):
        cls.objects.filter(id=id).update(occupant_count =new_occupant)
        
class UserProfile(models.Model):
    '''
    class that saves the user data 
    '''
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True )
    name = models.CharField(max_length = 100,null = True)
    identification = models.IntegerField(null = True) 
    neighborhood = models.ForeignKey(Neighborhood, on_delete = models.CASCADE, null=True)
    location = models.CharField(max_length = 100,null = True)
    avatar = models.ImageField(upload_to = 'avatar/',null = True)  
    def __str__(self):
       return self.name
    
    def save_profile(self):
        self.save()

    @classmethod
    def delete_profile(cls,id):
        cls.objects.filter(id).delete()
    @classmethod
    def update_profile(cls,id,new_name):
        cls.objects.filter(id=id).update(name = new_name)

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
    neighborhood = models.ForeignKey(Neighborhood, on_delete = models.CASCADE, null=True)
    email= models.CharField(max_length = 100)
    def __str__(self):
       return self.name
    
    def save_business(self):
        self.save()

    @classmethod
    def delete_business(cls,id):
        cls.objects.filter(id).delete()
    @classmethod
    def update_business(cls,id,new_name):
        cls.objects.filter(id=id).update(name = new_name)

    @classmethod
    def search_business(cls, searched_business):
        business = cls.objects.filter(name__icontains=searched_business)

        return business

class Post(models.Model):
   '''
   model that saves posts for the neighborhood 
   '''
   title = models.CharField(max_length  = 100,null = True)
   post = models.TextField(max_length=100,null = True)
   profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   time = models.DateTimeField(auto_now_add=True,null = True)

class Services(models.Model):
   '''
   model that saves the services data
   '''
   police_station = models.CharField(max_length = 30,blank = True)
   police_no = models.IntegerField(10,blank = True)
   police_location = models.CharField(max_length = 30,blank = True)
   healthcare_centre = models.CharField(max_length = 30,blank = True)
   healthcare_no = models.IntegerField(10,blank = True)
   healthcare_location = models.CharField(max_length = 30 ,blank = True)