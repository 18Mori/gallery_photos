from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import userProfile
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ['bio']
