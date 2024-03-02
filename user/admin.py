from django.contrib import admin
from .models import UserModel
from .forms import CreateUser,ChangeDetails
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    ordering = ['email']
    add_form = CreateUser
    form = ChangeDetails
    model = UserModel
    list_display = ['email','first_name','last_name','mobile_number']
    list_filter = ['email','first_name','last_name','mobile_number']
    list_display_links = ['email']
    search_fields = ['email','first_name','last_name','mobile_number']


admin.site.register(UserModel,UserModelAdmin)
    