# Generated by Django 4.2.4 on 2023-08-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_name',
        ),
        migrations.AddField(
            model_name='recipe',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='picture',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=250, null=True),
        ),
    ]