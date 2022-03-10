from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, "index.html", {})

def create_account_view(request):
    return render(request, "createAccount.html", {})

def account_hub_view(request):
    return render(request, "accountHub.html", {})

def login_view(request):
    return render(request, "login.html", {})

def search_view(request):
    return render(request, "searchResults.html", {})