# Generated by Django 4.0.3 on 2022-03-29 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_profile_ingredients_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ingredients_list',
        ),
        migrations.AlterField(
            model_name='profile',
            name='ingredients',
            field=models.JSONField(default=list, verbose_name='Ingredients'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='utensils',
            field=models.JSONField(default=list, verbose_name='Utensils'),
        ),
    ]