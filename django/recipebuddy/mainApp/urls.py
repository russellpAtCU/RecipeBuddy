from unicodedata import name
from django.urls import path

from . import views

urlpatterns =  [
    path('', views.home_view, name='index'),
    path('create-account/', views.create_account_view, name='create-account'),
]