from email.policy import default
from sqlite3 import Date
from urllib import request
import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, primary_key=True)
    ingredients = models.TextField("Ingredients", default='')
    utensils = models.TextField("Utensils", default='')
    
    #ingredients = models.JSONField(default=list, verbose_name="Ingredients")
    #utensils = models.JSONField(default=list, verbose_name="Utensils")

    def get_user(self):
        return self.user

    def get_utensils(self):
        return self.utensils

    def get_ingredients(self):
        return self.ingredients

    def __str__(self):
        return self.user.get_username()
    
    

class Recipe(models.Model):
    class Rating():
        user = models.ForeignKey(Profile, on_delete=models.CASCADE)
        rating: int
    class Comment():
        user: models.ForeignKey(Profile, on_delete=models.CASCADE)
        content: str
        date: Date
    utensils = list[str]
    author = Profile
    instructions = list[str]
    ratings = list[Rating]
    comments = list[Comment]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipe_name = models.CharField('Recipe name', blank=True, max_length=200)
    recipe_ingredients = models.TextField(help_text='Enter as a list separated by commas', default="")
    date = models.DateField('published', default=Date.today)

