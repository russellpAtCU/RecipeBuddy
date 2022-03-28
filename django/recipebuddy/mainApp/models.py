from sqlite3 import Date
import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# - Create a whole NewUser class with all fields

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    ingredients = models.TextField("Ingredients", default='')
    utensils = models.TextField("Utensils", default='')

class Recipe(models.Model):
    class Rating():
        user = models.ForeignKey(Profile, on_delete=models.CASCADE)
        rating: int
    class Comment():
        user: models.ForeignKey(Profile, on_delete=models.CASCADE)
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

