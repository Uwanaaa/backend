from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def email_validate(self,email):
       try:
           re.match(EMAIL_REGEX,email)
           return email
       except ValidationError:
           raise ValueError(_("Provide a valid email address"))
        


    def create_user(self, email, password, first_name, last_name, mobile_number, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not first_name:
            raise ValueError(_("First name needs to be provided"))
        
        if not last_name:
            raise ValueError(_("Last name needs to be provided"))
        
        if not mobile_number:
            raise ValueError(_("Mobile number needs to be provided"))
        
        if email:
          email = self.normalize_email(email)
          email= self.email_validate(email)
        else:
            raise ValueError(_("Email address should be provided"))


        user = self.model(
            email=email, 
            first_name = first_name,
            last_name = last_name,
            mobile_number = mobile_number,
            **extra_fields)
        
        user.set_password(password)
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        
        
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password, mobile_number, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

    
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(first_name, last_name, email, password, mobile_number, **extra_fields)
