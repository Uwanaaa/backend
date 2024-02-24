from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def signup(request):

    if request.method == 'POST':
        form = forms.CreateUser(request.POST)

        if form.is_valid():
         form.save()
         email = form.cleaned_data['email']
         password = form.cleaned_data['password1']

         user = authenticate(request,email=email,password=password)
         login(request,user)
         messages.success(request,"Logged in Successfully")
         return redirect('/home')
    else:
          form = forms.CreateUser()

    return render(request,"user/homepage.html",{'form':form})


def login_user(request):
    form = forms.LoginUser()

    if request.POST:
         email = request.POST['username']
         password = request.POST['password']

         user = authenticate(request,email=email,pasword=password)

         if user is not None:
            login(request,user)
            return redirect('/home')
         else :
            messages.error(request,'User does not exist')
    else:
          form = forms.LoginUser()

    return render(request,"user/homepage.html",{'form':form})
    


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


def setup_camera(request):

    if request.method == 'POST':
        form = forms.SetupCamera(request.POST)

        if form.is_valid():
            HttpResponse(form.cleaned_data)
        else:
            messages.error(request,'Input is invalid')
    else:
        form = forms.SetupCamera()
    
    return render(request,'user/setup.html',{'form':form})

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

def settings(request):
    pass

def dashboard(request):
    pass