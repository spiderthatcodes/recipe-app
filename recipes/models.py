from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=250, null=True)
    picture = models.URLField(null=True)
    description = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
