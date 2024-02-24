from .models import UserModel
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm,PasswordResetForm
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


class ForgotPassword(PasswordResetForm):
    email = forms.EmailField(required=True)


class SetupCamera(forms.Form):
    Choices = (
        (1,'One'),
        (2,'Two'),
        (3,'Three'),
    )
    amount_of_cameras = forms.ChoiceField(choices=Choices,attrs={'placeholder':'Amount of Cameras'})
    ip_address_1 = forms.GenericIPAddressField(required=True,attrs={'placeholder':'IP address(Camera 1)'})
    ip_address_2 = forms.GenericIPAddressField(attrs={'placeholder':'IP address(Camera 2)'})
    ip_address_3 = forms.GenericIPAddressField(attrs={'placeholder':'IP address(Camera 3)'})


class AnimalType(forms.Form):
    Choices = (
        ('pig','Pig'),
        ('sheep','Sheep'),
        ('goat','Goat'),
        ('chicken','Chicken'),
        ('cow','Cow')

    )
    type_of_animal = forms.ChoiceField(choices=Choices,attrs={'placeholder':'Type of Animal'})
    animal_1 = forms.CharField(attrs={'placeholder':'Animal to monitor with camera 1'},required=True)
    animal_2 = forms.CharField(attrs={'placeholder':'Animal to monitor with camera 2'})
    animal_3 = forms.CharField(attrs={'placeholder':'Animals to monitor with camera 3'})

