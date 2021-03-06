# Generated by Django 4.0.3 on 2022-04-19 14:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ingredients', models.JSONField(default=list, verbose_name='Ingredients')),
                ('utensils', models.JSONField(default=list, verbose_name='Utensils')),
                ('recipe_ids', models.TextField(default=None, verbose_name='Recipes')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipe_name', models.CharField(blank=True, max_length=200, verbose_name='Recipe name')),
                ('author', models.CharField(blank=True, max_length=35, verbose_name='Author')),
                ('instructions', models.TextField(verbose_name='Instructions')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('recipe_ingredients', models.TextField(blank=True, max_length=300, verbose_name='Ingredients')),
                ('recipe_utensils', models.TextField(blank=True, max_length=300, verbose_name='Utensils')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Created')),
            ],
        ),
    ]
