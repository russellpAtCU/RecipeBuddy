import uuid
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse
from .models import Recipe, Profile

# Create views here

search_results = []


def search_recipes(search_str, type):
    results = []
    recipes = Recipe.objects.all()
    search_words = search_str.split(', ')
    if search_words == ['']:
            results = recipes
    else:
        for recipe in recipes:
            
            if type == 'ingredient':
                print(recipe.get_ingredients_as_list())
                print(any(words in search_words for words in recipe.get_ingredients_as_list()))
                if any(words in search_words for words in recipe.get_ingredients_as_list()):
                    results.append(recipe)
            if type == 'utensil':
                print(recipe.get_utensil_as_list())
                print(any(words in search_words for words in recipe.get_utensils_as_list()))
                if any(words in search_words for words in recipe.get_utensils_as_list()):
                    results.append(recipe)
            if type == 'keyword':
                if any(words in search_words for words in recipe.get_name_as_list()) or any(words in search_words for words in recipe.get_utensils_as_list()) or any(words in search_words for words in recipe.get_ingredients_as_list()):
                    results.append(recipe)

    global search_results
    search_results = results

    return results


def home_view(request):
    if request.method == "POST":
        search_type = (str)(request.POST.get('search_type'))
        search_str = (str)(request.POST.get('search_str'))
        search_recipes(search_str=search_str, type=search_type)
        if search_str != '':
            query_ext = search_str.replace(' ', '+')
        else:
            query_ext = '+'
        return redirect(reverse('search',kwargs={'query': query_ext}))
    return render(request, "index.html", {})


def search_view(request, query):
    if request.method == 'POST':
        search_type = (str)(request.POST.get('search_type'))
        search_str = (str)(request.POST.get('search_str'))
        results = search_recipes(search_str=search_str, type=search_type)
        #query_ext = search_str.replace(' ', '+')
        return redirect(reverse('search', kwargs={'query': query}))
    else:
        results = search_results
    
    return render(request, "searchResults.html", {'results': results})


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

    # if request.method == 'POST':
    #     del_id = request.POST.get('if_delete')
    #     if del_id != '':
    #         profile.del_recipe(recipe_id=del_id)
    #         del_id = uuid.UUID(del_id)
    #         to_delete = Recipe.objects.get(id=del_id)
    #         to_delete.delete()
    #         #return redirect(reverse('account-hub'))

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


def recipe_view(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe_comments = recipe.get_recipe_comments()
    recipe_ingredients = recipe.get_recipe_ingredients().split(', ')
    recipe_utensils = recipe.get_recipe_utensils().split(', ')
    recipe_instructions = recipe.get_recipe_instructions().split("(,)")
    return render(request, "recipePage.html", {'recipe':recipe, 'recipe_ingredients':recipe_ingredients, 'recipe_utensils':recipe_utensils, 'recipe_instructions':recipe_instructions, 'recipe_comments':recipe_comments})


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

