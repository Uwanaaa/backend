from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from rest_framework import serializers
from django.utils import timezone
# Create your models here.

class UserModel(AbstractUser):
    username = None
    email = models.EmailField(_("Email"),unique=True,max_length=50)
    mobile_number = models.CharField(_("Mobile number"),max_length=20)
    first_name = models.CharField(_("First Name"),max_length=20)
    last_name = models.CharField(_("Last name"),max_length=20)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name","mobile_number"]

    objects = UserManager()

    def __str__(self):
        return self.email
    

