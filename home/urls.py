from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('open-cam/',views.open_cam,name='open_cam'),
    path('open-camera/',views.open_camera,name='open_camera')
]