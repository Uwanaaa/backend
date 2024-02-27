from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from . import forms
from settings.views import profile
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import UserModelSerializer
from .models import UserModel
import json

# Create your views here.
@api_view(['GET','POST'])
def signup(request):

    if request.method == 'POST':
        input_data = json.loads(request.body.decode('utf-8'))
        form = forms.CreateUser(input_data)
        print(input_data)

        if form.is_valid():
         form.save()
         print(form.cleaned_data)
         password = form.cleaned_data['password1']
         email = form.cleaned_data['email']

         user = authenticate(request,email=email,password=password)
         login(request,user)
         HttpResponse(request,"Logged in Successfully")
         request.session['user_id'] = user.id
         request.session['password'] = request.POST['password']
         return render(request,'user/redirect.html')
        else:
            print(form.errors)
    else:
          form = forms.CreateUser()

    return render(request,"user/homepage.html",{'form':form})

@api_view(['GET','POST'])
def login_user(request):
    form = forms.LoginUser()

    if request.method == 'POST':
         input_data = json.loads(request.body.decode('utf-8'))
         email = input_data['username']
         password = input_data['password']

         user = authenticate(request,email=email,pasword=password)

         if user is not None:
            login(request,user)
            profile(request,user)
            return redirect('/settings/profile')
         else :
            HttpResponse(request,'User does not exist')
    else:
          form = forms.LoginUser()

    return HttpResponse("This the login page")
    


def logout(request):

    logout(request)
    return redirect('/home')


#@login_required
def homepage(request):
   return render(request,"user/home.html")

def forgot_password(request):

    if request.method == 'POST':
        form = forms.ForgotPassword(request.POST)
        email = form.cleaned_data['email']
    else:
        form = forms.ForgotPassword()
    
    return render(request,'user/homepage.html',{'form':form})


@api_view(['GET','POST'])
def setup_camera(request):

    if request.method == 'POST':
        input_data = json.loads(request.body.decode('utf-8'))
        form = forms.SetupCamera(input_data)
        

        if form.is_valid():
            HttpResponse(form.cleaned_data)
            print(form.cleaned_data)
        else:
            return HttpResponse('Input data is invalid')
    else:
        form = forms.SetupCamera()
    
    return HttpResponse('Connected to the server')
    #return render(request,'user/setup.html',{'form':form})



def animal_setup(request):

    if request.method == 'POST':
        form = forms.AnimalType(request.POST)

        if form.is_valid():
            type_of_animal = form.cleaned_data['type_of_animal']
            animal_1 = form.cleaned_data['animal_1']
            animal_2 = form.cleaned_data['animal_2']
            animal_3 = form.cleaned_data['animal_3']
        else:
            messages.error(request,'User input invalid')
    else:
        form = forms.AnimalType()

    return render(request,'user/setup.html',{'form':form})


def farm_monitor(request):
    pass


def data_manager(request):
    pass


def dashboard(request):
    pass