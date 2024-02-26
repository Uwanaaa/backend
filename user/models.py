from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from rest_framework import serializers
# Create your models here.

class UserModel(AbstractUser):
    username = None
    email = models.EmailField(_("Email"),unique=True)
    mobile_number = models.CharField(_("Enter your phone number"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    

