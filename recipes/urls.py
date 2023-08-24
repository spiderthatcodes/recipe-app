from django.urls import path
from .views import show_recipes, recipe_list

urlpatterns = [
    path("recipes/", recipe_list),
    path("recipes/<int:id>", show_recipes, name="show_recipes"),
]
