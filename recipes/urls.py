from django.urls import path
from .views import show_recipes

urlpatterns = [
    path("recipes/<int:id>", show_recipes, name="show_recipes")
]
