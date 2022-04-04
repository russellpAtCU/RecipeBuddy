
from multiprocessing import context
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.generic.base import RedirectView
from .models import Recipe, Profile

# Create views here
# - Should migrate to view classes

def home_view(request):
    return render(request, "index.html", {})

def create_account_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirm_pass')
        ingredients = request.POST.get('ingredients')
        utensils = request.POST.get('utensils')

        # Create function to parse utensils/ingredients
        # Fix button functionality
        # Add utensil/ingredient button should clear text field and add item to the respective list
        if username != '' or password != '':
            if password == confirm_pass:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username not available')
                    return redirect('/app/create-account')
                else:
                    ingredients_list = ingredients.split(',')
                    utensils_list = utensils.split(',')
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
    ingredients = Profile.get_ingredients
    utensils = Profile.get_utensils
    request.GET[utensils]
    request.GET[ingredients]
    return render(request, "accountHub.html", {})

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

def recipe_view(request):
    id = Recipe.id
    return render(request, "recipePage.html", {'id' : id})

def create_recipe_view(request):
    return render(request, 'recipeCreation.html', {})