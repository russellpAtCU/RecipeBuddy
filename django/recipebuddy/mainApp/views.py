from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Recipe

# Create your views here.

def home_view(request):
    users = User.objects.all
    return render(request, "index.html", {})

def create_account_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_pass = request.POST['confirm_pass']
        if password == confirm_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username not available')
                return redirect('/app/create-account')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('/app')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('/app/create-account')
    return render(request, "createAccount.html", {})

def account_hub_view(request):
    return render(request, "accountHub.html", {})

def login_view(request):
    return render(request, "login.html", {})

def search_view(request):
    return render(request, "searchResults.html", {})

def recipe_view(request):
    id = Recipe.id
    return render(request, "recipePage.html", {'id': id})

def create_recipe_view(request, id):
    return render(request, 'recipeCreation.html',)