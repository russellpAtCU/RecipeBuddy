from email.policy import default
from mimetypes import init
from sqlite3 import Date
from urllib import request
import uuid
from django.db import models
from django.contrib.auth.models import User
from pkg_resources import require

# Create your models here.

# Working on create_recipe_view

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, primary_key=True)
    #ingredients = models.TextField("Ingredients", default='')
    #utensils = models.TextField("Utensils", default='')
    
    ingredients = models.JSONField(default=list, verbose_name="Ingredients")
    utensils = models.JSONField(default=list, verbose_name="Utensils")
    recipes = models.JSONField(default=list, verbose_name="Recipes")

    def get_recipes(self):
        return self.recipes

    def get_ingredients(self):
        return self.ingredients

    def get_utensils(self):
        return self.utensils

    def get_user(self):
        return self.user

    def __str__(self):
        return self.user.get_username()
    
    

class Recipe(models.Model):
    class Rating():
        user = Profile
        rating = int
    class Comment():
        user = Profile
        content = str
        date = Date

        def __str__(self):
            return self.user.get_username
            
    recipe_name = models.CharField('Recipe name', blank=True, max_length=200)
    author = models.CharField('Author', blank=True, max_length=35)
    instructions = models.JSONField(default=tuple, verbose_name="Instructions")
    ratings = models.JSONField(default=list[Rating], verbose_name="Ratings")
    comments = models.JSONField(default=list[Comment], verbose_name="Comments")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipe_ingredients = models.JSONField(default=list, verbose_name="Ingredients")
    recipe_utensils = models.JSONField(default=list, verbose_name="Utensils")
    date = models.DateField('Created', default=Date.today)

    def get_id(self):
        return self.id

    def __str__(self):
        return self.recipe_name

    

