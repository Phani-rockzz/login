from django import forms
from django.contrib.auth.models import User
from django.core import validators
from phani.models import User
from phani.models import UserProfileInfo






class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')








class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms .CharField(widget=forms.Textarea)


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =  '__all__'

  
      
   