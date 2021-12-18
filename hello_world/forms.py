from django import forms 
from hello_world.models import UserProfileInfo
from django.contrib.auth.models import User
 
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta(): #the inner class of your model class.
        model = User
        fields = ('username','password','email')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }
 
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('occupation','company','hobby')
        widgets = {
            'occupation':forms.Textarea(attrs={'class':'form-control'}),
            'company':forms.Textarea(attrs={'class':'form-control'}),
            'hobby':forms.Textarea(attrs={'class':'form-control'}),
        }