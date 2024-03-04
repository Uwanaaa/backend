from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
#from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from settings.views import profile
from rest_framework.decorators import api_view
from .serializers import UserModelSerializer
from google.auth.transport import requests
from google.oauth2 import id_token
from dotenv import load_dotenv
from .models import UserModel
from . import forms
import json
import os



# Create your views here.
@api_view(['GET','POST'])
def signup(request):

    if request.method == 'POST':
        input_data = json.loads(request.body.decode('utf-8'))
        form = forms.CreateUser(input_data)
        print(input_data)

        if form.is_valid():
         form.save()
         password = form.cleaned_data['password1']
         email = form.cleaned_data['email']
     

         user = authenticate(request,email=email,password=password)

         if user is not None:
            login(request,user)
            request.session['user_id'] = user.id
            request.session['password'] = user.password
            Response({"status":"Logged in Successfully","pass":"true"})
            #return render(request,'user/redirect.html')
         else:
            Response({"status":"User exist already","pass":"false"})
        else:
            data_error = form.errors.as_json()
            print(data_error)
            HttpResponse(data_error)

    else:
          form = forms.CreateUser()

    return JsonResponse({"status":"Data sent"})
    #return render(request,"user/homepage.html",{'form':form})

@api_view(['GET','POST'])
def login_user(request):

    if request.method == 'POST':
        input_data = json.loads(request.body.decode('utf-8'))
        form = forms.LoginUser(input_data)
        print(input_data)

        if form.is_valid():
         password = form.cleaned_data['password1']
         email = form.cleaned_data['email']
     

         user = authenticate(request,email=email,password=password)

         if user is not None:
            login(request,user)
            request.session['user_id'] = user.id
            request.session['password'] = user.password
            JsonResponse({"status":"Logged in Successfully","pass":"true"})
            #return render(request,'user/redirect.html')
         else:
            JsonResponse({"status":"User exist already","pass":"false"})
        else:
            data_error = form.errors.as_json()
            print(data_error)
            HttpResponse(data_error)

    else:
          form = forms.CreateUser()

    return JsonResponse({"status":"Data sent"})
    #return render(request,"user/homepage.html",{'form':form})

        
    
#@api_view(['GET'])
#def google_auth(request):
    load_dotenv()
    redirect_uri = request.build_absolute_uri('/auth/google/callback/')
    client_id = os.environ['CLIENT_ID']
    auth_url = f'https://accounts.google.com/o/oauth2/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=email%20profile'  # Google OAuth URL
    return redirect(auth_url)

#@api_view(['GET'])
#def authenticated(request):
    token = request.POST['credential']

    try:
        data = id_token.verify_oauth2_token(
            token, requests.Request(),os.environ['CLIENT_ID']
        )
    except ValueError:
        return HttpResponse(status=403)
    
    email = data.get('email')
    print(email)
    account = SocialAccount.objects.filter(provider='google',uid=email).first()

    if account:
        user = account.user
        print(user)
    else:
        print("User doesn't exist")

    return render(request,'user/redirect.html')


def logout_user(request):
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
            JsonResponse(form.cleaned_data)
            print(form.cleaned_data)
        else:
            return JsonResponse('Input data is invalid')
    else:
        form = forms.SetupCamera()
    
    return JsonResponse('Connected to the server')
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