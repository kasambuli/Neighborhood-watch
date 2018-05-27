from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Neighborhood,Business,UserProfile

# profile form
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user','name','avatar','neighborhood','location']

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ['name','location','occupant_count']
