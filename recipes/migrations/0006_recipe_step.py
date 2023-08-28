# Generated by Django 4.2.4 on 2023-08-28 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe_Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', models.TextField()),
                ('order', models.PositiveIntegerField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='recipes.recipe')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]