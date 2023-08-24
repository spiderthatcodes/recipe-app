from django.shortcuts import render, get_object_or_404
from .models import Recipe
from .forms import RecipeForm


def show_recipes(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        "recipe_object": recipe,
    }

    return render(request, "detail.html", context)

def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list": recipes,
    }
    return render(request, "list.html", context)


def create_recipe(request):
    form = RecipeForm()
