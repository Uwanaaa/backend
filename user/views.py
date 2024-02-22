from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .forms import CreateUser,ChangeDetails,LoginUser

# Create your views here.
def signup(request):

    if request.POST:
        form = CreateUser(request.POST)
        if form.is_valid():
         email = request.POST['email']
         password = request.POST['password']

         form.save()

         user = authenticate(request,email=email,password=password)
         if user is not None:
             login(request,user)
             messages.success("Logged in Successfully")
             return redirect('homepage')
         else:
          messages.error("Retry signing up")
    else:
          form = CreateUser()

    return render(request,"user/homepage.html",{'form':form})


def login(request):

    if request.POST:
        form = LoginUser(request.POST)
        if form.is_valid:
         email = request.POST['username']
         password = request.POST['password']

         user = authenticate(request,email=email,pasword=password)

        if user is not None:
            login(request,user)
            return redirect('homepage')
        else :
            messages.error(request,'User does not exist')
    else:
          form = LoginUser()
    
    return render(request,"user/homepage.html",{'form':form})
    


def logout(request):

    logout(request)
    return redirect('homepage')


def homepage(request):
   return render(request,"user/index.html")