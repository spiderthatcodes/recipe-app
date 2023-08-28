from django.contrib import admin
from .models import Recipe, Recipe_Step, Ingredient

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "id"
    )


@admin.register(Recipe_Step)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = (
        "recipe_title",
        "order",
        "id"
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "recipe_title",
        "food_item",
        "id"
    )
