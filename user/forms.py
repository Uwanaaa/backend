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
        ('','Number of Cameras'),
        (1,'One'),
        (2,'Two'),
        (3,'Three'),
    )
    amount_of_cameras = forms.ChoiceField(choices=Choices)
    ip_address_1 = forms.GenericIPAddressField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter IP Address 1'}))
    ip_address_2 = forms.GenericIPAddressField(widget=forms.TextInput(attrs={'placeholder': 'Enter IP Address 2'}))
    ip_address_3 = forms.GenericIPAddressField(widget=forms.TextInput(attrs={'placeholder': 'Enter IP Address '}))


class AnimalType(forms.Form):
    Choices = (
        ('','Type of Animal'),
        ('pig','Pig'),
        ('sheep','Sheep'),
        ('goat','Goat'),
        ('chicken','Chicken'),
        ('cow','Cow')

    )
    type_of_animal = forms.ChoiceField(choices=Choices)
    animal_1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Animal 1'}),required=True)
    animal_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Animal 2'}))
    animal_3 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Animal 3'}))

