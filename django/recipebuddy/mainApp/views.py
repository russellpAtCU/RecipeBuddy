from multiprocessing import context
from urllib import request
from uuid import UUID, uuid4
import uuid
from django.forms import UUIDField
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse
from django.views.generic.base import RedirectView
from .models import Recipe, Profile

# Create views here
# - Should migrate to view classes

def search_recipes(search_str, type):
    results = list[Recipe]
    recipes = Recipe.objects.all()
    search_words = search_str.split(' ')
    for recipe in recipes:
        if type == 'ingredient':
            if any(search_words) in recipe.get_ingredients:
                results.append(recipe)
        if type == 'utensil':
            if any(search_words) in recipe.get_utensils:
                results.append(recipe)
        if type == 'keyword':
            if any(search_words) in recipe.__str__:
                results.append(recipe)
    return results

def home_view(request):
    return render(request, "index.html", {})


def create_account_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirm_pass')
        ingredients = request.POST.get('ingredients_list')
        utensils = request.POST.get('utensils_list')

        if username != '' or password != '':
            if password == confirm_pass:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username not available')
                    return redirect('/app/create-account')
                else:
                    if ingredients is not None:
                        ingredients_list = ingredients.split(',')
                    else:
                        ingredients_list = ''
                    if utensils is not None:
                        utensils_list = utensils.split(',')
                    else:
                        utensils_list = ''
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    prof = Profile(user=user, ingredients=ingredients_list, utensils=utensils_list)
                    prof.save()
                    login(request, user)
                    return redirect('/app')
            else:
                messages.info(request, "Passwords do not match")
                return redirect('/app/create-account')
        else:
            messages.info(request, "Username and password are required")
    return render(request, "createAccount.html", {})


def account_hub_view(request):
    profile = Profile.objects.get(user=request.user)
    ingredients = profile.get_ingredients
    utensils = profile.get_utensils()
    id_list = profile.get_recipe_ids().split(', ')
    recipes = []
    recipes_ingredients = []
    recipes_utensils = []
    if id_list != ['']:
        for id in id_list:
            id = uuid.UUID(id)
            recipe = Recipe.objects.get(id=id)
            recipes.append(recipe)
            recipe_ingr = recipe.get_recipe_ingredients().split(', ')
            recipes_ingredients.append(recipe_ingr)
            recipe_utn = recipe.get_recipe_utensils().split(', ')
            recipes_utensils.append(recipe_utn)

    recipe_count = recipes.__len__

    return render(request, "accountHub.html", {'profile':profile, 'utensils':utensils, 'ingredients':ingredients, 'recipes':recipes,
     'recipes_ingredients':recipes_ingredients, 'recipes_utnensils':recipes_utensils, 'count':recipe_count, 'id_list':id_list})


def logout_view(request):
    logout(request)
    return redirect('/app')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/app/account-hub')
        else:
            messages.info(request, 'invalid credentials or user does not exist')
    return render(request, "login.html", {})


def search_view(request):
    return render(request, "searchResults.html", {})


def recipe_view(request, id):
    #id = Recipe.objects.get(id=request.id)
    recipe = Recipe.objects.get(id=id)
    recipe_ingredients = recipe.get_recipe_ingredients().split(', ')
    recipe_utensils = recipe.get_recipe_utensils().split(', ')
    recipe_instructions = recipe.get_recipe_instructions().split("(,)")
    return render(request, "recipePage.html", {'recipe':recipe, 'recipe_ingredients':recipe_ingredients, 'recipe_utensils':recipe_utensils, 'recipe_instructions':recipe_instructions})


def create_recipe_view(request):
    if request.method == 'POST':
        prof = Profile.objects.get(user=request.user)
        username = prof.get_user().get_username()
        steps = request.POST.get('all_steps')
        #instructions = steps.split('(,)')
        recipe_name = request.POST.get('title')
        recipe_ingr = request.POST.get('recipe_ingredients')
        recipe_utn = request.POST.get('recipe_utensils')

        recipe = Recipe(recipe_name=recipe_name, instructions=steps, author=username, recipe_ingredients=recipe_ingr, recipe_utensils=recipe_utn)
        recipe.save()
        prof.add_recipe((str)(recipe.id))
        prof.save()
        return redirect(reverse("recipe", kwargs={'id':(str)(recipe.id)}))

    return render(request, 'recipeCreation.html', {})

