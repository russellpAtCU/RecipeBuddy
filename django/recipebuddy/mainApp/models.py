from pickletools import read_stringnl_noescape
from sqlite3 import Date
import uuid
from datetime import datetime
from django.db import models
from django.shortcuts import render

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    ingredients = list[str]
    utensils = list[str]
    loggedIn = bool
    
    def logout():
        User.loggedIn = False
   

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

