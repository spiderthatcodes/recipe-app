from django.shortcuts import render
from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipes": recipes,
    }

    return render(request, "detail.html", context)
