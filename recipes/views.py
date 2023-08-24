from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm


# this controller is for the details page
def show_recipes(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        "recipe_object": recipe,
    }

    return render(request, "detail.html", context)

# list page controller
def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list": recipes,
    }
    return render(request, "list.html", context)

# create recipe controller
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('recipe_list')
    else:
        form = RecipeForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)
