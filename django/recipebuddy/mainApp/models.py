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
    #recipes = models.JSONField(default=list, verbose_name="Recipes")

    recipe_ids = models.TextField(verbose_name="Recipes", default='', blank=True, max_length=None)

    # NEED TO REWORK MODELS. Store lists as text fields separated by ', '
    # JSON fields don't allow the same functionality as lists

    def del_recipe(self, recipe_id):
        if (self.recipe_ids.find(recipe_id) + 36 == ','):
            self.recipe_ids.replace(recipe_id + ',', '')
        else: # last in list case
            self.recipe_ids.replace(recipe_id, '')

    def add_recipe(self, recipe_id):
        if self.recipe_ids == '':
            self.recipe_ids += (recipe_id)
        else:
            self.recipe_ids += ', ' + (recipe_id)
    
    def get_recipe_ids(self):
        return self.recipe_ids

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
    instructions = models.TextField(verbose_name="Instructions", max_length=None)
    ratings = models.JSONField(default=list[Rating], verbose_name="Ratings")
    comments = models.JSONField(default=list[Comment], verbose_name="Comments")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipe_ingredients = models.TextField(verbose_name="Ingredients", max_length=300, blank=True)
    recipe_utensils = models.TextField(verbose_name="Utensils", blank=True, max_length=300)
    date = models.DateField('Created', default=Date.today)

    def get_recipe_utensils(self):
        return self.recipe_utensils

    def get_recipe_comments(self):
        return self.comments

    def get_recipe_ratings(self):
        return self.ratings

    def get_ingredients_as_list(self):
        ing = self.recipe_ingredients.split(', ')
        return ing
    
    def get_utensils_as_list(self):
        utn = self.recipe_utensils.split(', ')
        return utn
    
    def get_name_as_list(self):
        keywords = self.recipe_name.split(' ')
        return keywords

    def get_recipe_ingredients(self):
        return self.recipe_ingredients

    def get_recipe_instructions(self):
        return self.instructions

    def get_id(self):
        return self.id

    def __str__(self):
        return self.recipe_name

    

