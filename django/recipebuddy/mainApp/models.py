from sqlite3 import Date
import this
import uuid
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    username = models.CharField(max_length=30, default='', unique=True)
    password = models.CharField(max_length=20, default='')

    ingredients = list[str]
    utensils = list[str]
    loggedIn = bool
    
    def logout():
        CustomUser.loggedIn = False
   

class Recipe(models.Model):
    class Rating():
        user = User
        rating: int
    class Comment():
        user: User
        content: str
        date: Date
    utensils = list[str]
    author = User
    instructions = list[str]
    ratings = list[Rating]
    comments = list[Comment]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipe_name = models.CharField('Recipe name', blank=True, max_length=200)
    recipe_ingredients = models.TextField(help_text='Enter as a list separated by commas', default="")
    date = models.DateField('published', default=Date.today)

