from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Neighborhood,Business,UserProfile,Post,Services

# profile form
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user','name','avatar','neighborhood','location']

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ['name','location','occupant_count']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','post','profile','user']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name','user','neighborhood','email']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['police_station','police_no','police_location','healthcare_centre','healthcare_no','healthcare_location']