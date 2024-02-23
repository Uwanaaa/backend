from .models import UserModel
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django import forms


# - Form to create a user
class CreateUser(UserCreationForm):
     email = forms.EmailField(max_length=30,required=True)
     first_name = forms.CharField(max_length=30,required=True)
     last_name = forms.CharField(max_length=30,required=True)
     mobile_number = forms.CharField()
     class Meta:
        model = UserModel
        fields = ('first_name','last_name','email','mobile_number')

# - Form to login a user
class LoginUser(AuthenticationForm):

    remember_me = forms.BooleanField(required=False)

    class Meta:
        fields = ('email','password')

class ChangeDetails(UserChangeForm):

    class Meta:
        model = UserModel
        fields = ('first_name','last_name','email','password','mobile_number')