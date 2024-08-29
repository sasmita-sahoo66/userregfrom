from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta :
        model=User
        fields=['username','email','password']
        # fields='__all__'
        widgets={'password':forms.PasswordInput()}
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['profile_pic','address']
        # fields='__all__'
        