from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpRequest
from django.contrib.auth import get_user_model


class UserBackend(BaseBackend):
    def authenticate(self, request: HttpRequest | None, email: str, password: str) -> AbstractBaseUser:
         model = get_user_model()

         try:
              user = model.objects.get(email=email)
         except model.DoesNotExist:
              return None
         else:
              if user.check_password(password):
                   return user
     
     
    def get_user(self,email):
         model = get_user_model()

         try:
              user = model.objects.get(email=email)
              return user
         except model.DoesNotExist:
              return None