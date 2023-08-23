from django.urls import path
from .views import recipe_list

urlpatterns = [
    path("recipes", recipe_list, name="recipe_list")
]
