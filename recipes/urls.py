from django.urls import path
from .views import show_recipes, recipe_list, create_recipe

urlpatterns = [
    path("recipes/", recipe_list, name='recipe_list'),
    path("recipes/<int:id>", show_recipes, name="show_recipes"),
    path("recipes/add/", create_recipe, name="create_recipe")
]
