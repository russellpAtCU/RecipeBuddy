from unicodedata import name
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns =  [
    path('', views.home_view, name='index'),
    path('create-account/', views.create_account_view, name='create-account'),
    path('account-hub/', views.account_hub_view, name='account-hub'),
    path('login/', views.login_view, name='login'),
    path('search/<str:query>', views.search_view, name='search'),
    path('recipe/<uuid:id>', views.recipe_view, name='recipe'),
    path('create-recipe/', views.create_recipe_view, name='create-recipe'),
    path('logout/', views.logout_view, name='logout'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)