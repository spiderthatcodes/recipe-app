from django.db import models
from django.conf import settings

class Recipe(models.Model):
    title = models.CharField(max_length=250)
    picture = models.URLField(blank=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='recipes',
        on_delete=models.CASCADE,
        null=True
    )


class Recipe_Step(models.Model):
    instruction = models.TextField()
    order = models.PositiveIntegerField() # this should be unique
    recipe = models.ForeignKey(
        'Recipe',
        related_name='steps',
        on_delete=models.CASCADE
    )

    def recipe_title(self):
        return self.recipe.title

    class Meta:
        ordering = ['order']


class Ingredient(models.Model):
    food_item = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        'Recipe',
        related_name='ingredients',
        on_delete=models.CASCADE
    )

    def recipe_title(self):
        return self.recipe.title

    class Meta:
        ordering = ['food_item']
