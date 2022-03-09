from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, "index.html", {})

def create_account_view(request):
    return render(request, "createAccount.html", {})