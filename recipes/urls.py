from django.urls import path
from .views import show_recipes, recipe_list, create_recipe, edit_recipe, delete_recipe

urlpatterns = [
    path("recipes/", recipe_list, name='recipe_list'),
    path("recipes/<int:id>", show_recipes, name="show_recipes"),
    path("recipes/add/", create_recipe, name="create_recipe"),
    path("recipes/<int:id>/edit", edit_recipe, name="edit_recipe"),
    path("recipes/<int:id>/delete", delete_recipe, name="delete_recipe")
]
