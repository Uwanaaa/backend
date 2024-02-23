from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateUser,ChangeDetails,LoginUser

# Create your views here.
def signup(request):

    if request.method == 'POST':
        form = CreateUser(request.POST)

        if form.is_valid():
         form.save()
         email = form.cleaned_data['email']
         password = form.cleaned_data['password1']

         user = authenticate(request,email=email,password=password)
         login(request,user)
         messages.success(request,"Logged in Successfully")
         return redirect('/home')
    else:
          form = CreateUser()

    return render(request,"user/homepage.html",{'form':form})


def login_user(request):
    form = LoginUser()

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
          form = LoginUser()

    return render(request,"user/homepage.html",{'form':form})
    


def logout(request):

    logout(request)
    return redirect('/home')


#@login_required
def homepage(request):
   return render(request,"user/home.html")