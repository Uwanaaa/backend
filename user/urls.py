from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout,name='logout'),
    path('home',views.homepage,name='home')
]