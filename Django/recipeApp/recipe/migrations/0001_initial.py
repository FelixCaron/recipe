# Generated by Django 4.2.6 on 2023-10-18 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergen_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_text', models.CharField(max_length=200)),
                ('ingredient_allergen_set', models.ManyToManyField(blank=True, to='recipe.allergen')),
            ],
        ),
        migrations.CreateModel(
            name='recipe_step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('recipe_ingredient_set', models.ManyToManyField(to='recipe.ingredient')),
                ('recipe_step_list', models.ManyToManyField(to='recipe.recipe_step')),
            ],
        ),
    ]
