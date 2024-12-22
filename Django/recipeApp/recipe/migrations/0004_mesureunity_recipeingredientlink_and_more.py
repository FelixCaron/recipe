# Generated by Django 4.2.6 on 2023-10-22 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_remove_recipe_recipe_ingredient_set_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MesureUnity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unity_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredientLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
                ('unity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.mesureunity')),
            ],
        ),
        migrations.DeleteModel(
            name='RecipeIngredientOrder',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_ingredients',
            field=models.ManyToManyField(through='recipe.RecipeIngredientLink', to='recipe.ingredient'),
        ),
    ]
