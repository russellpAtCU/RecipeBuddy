# Generated by Django 4.0.3 on 2022-04-14 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_alter_recipe_comments_alter_recipe_instructions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='comments',
            field=models.JSONField(default=list, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.JSONField(default=tuple, verbose_name='Instructions'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ratings',
            field=models.JSONField(default=list, verbose_name='Ratings'),
        ),
    ]
