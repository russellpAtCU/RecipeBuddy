from atexit import register
from tabnanny import verbose
from django.contrib import admin
from .models import Profile, Recipe
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.

admin.site.register(Profile)
admin.site.register(Recipe)