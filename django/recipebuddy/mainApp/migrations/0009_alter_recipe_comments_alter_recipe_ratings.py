# Generated by Django 4.0.3 on 2022-04-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_alter_recipe_comments_alter_recipe_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='comments',
            field=models.JSONField(default=list, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ratings',
            field=models.JSONField(default=list, verbose_name='Ratings'),
        ),
    ]
