from django.contrib import admin

from .models import CustomUser, Recipe

# Register your models here.
admin.site.register(Recipe)
#admin.site.register(CustomUser)