import uuid
from datetime import datetime
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Recipe name', blank=True, max_length=200)
    ingredients = models.TextField(help_text='Enter as a list separated by commas', default="")
    date = models.DateTimeField('published', default=datetime.now)
    
