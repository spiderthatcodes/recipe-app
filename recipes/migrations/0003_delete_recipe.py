# Generated by Django 4.2.4 on 2023-08-23 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_remove_recipe_recipe_name_recipe_created_on_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]