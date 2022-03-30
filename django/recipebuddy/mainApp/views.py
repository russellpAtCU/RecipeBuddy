from multiprocessing import context
import profile
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Recipe, Profile

# Create your views here.

def home_view(request):
    return render(request, "index.html", {})

def create_account_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_pass = request.POST['confirm_pass']
        ingredients = request.POST['ingredients']
        utensils = request.POST['utensils']

        # Create function to parse utensils/ingredients
        # Fix button functionality
        # Add utensil/ingredient button should clear text field and add item to the respective list
        if username is not '' or password is not '':
            if password == confirm_pass:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username not available')
                    return redirect('/app/create-account')
                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    prof = Profile(user=user, ingredients=ingredients, utensils=utensils)
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