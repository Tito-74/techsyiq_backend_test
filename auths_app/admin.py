from django.contrib import admin
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
  model = User
  add_form = CustomUserCreationForm
  # fieldsets = (
  #   *UserAdmin.fieldsets,
  #   (
  #     'User Roles',
  #     {
  #       'fields':(
  #         'is_admin',
  #         'is_staff',
  #       )
  #     }
  #   )
  # )

admin.site.register(User, CustomUserAdmin)