from sqlite3 import Date
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class User(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, default='')
    password = models.CharField(max_length=20, default='')
    ingredients = list[str]
    utensils = list[str]
    loggedIn = bool

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, **kwargs):
        User.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
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

