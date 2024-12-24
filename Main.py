import os
import django
import sys
import scrape_schema_recipe

sys.path.append("D:/gitrepos/recipe/Application/")

# Définir le chemin des paramètres Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipeApp.settings")
django.setup()

from Application.models_recipe.models import Recipe, Ingredient, RecipeStep, RecipeIngredientLink, RecipeStepOrder, MesureUnity, Allergen

def populate_database():
    # Ajouter des unités de mesure
    gram = MesureUnity.objects.get_or_create(unity_text="gram")[0]
    cup = MesureUnity.objects.get_or_create(unity_text="cup")[0]

    # Ajouter des allergènes
    peanut_allergen = Allergen.objects.get_or_create(allergen_text="Peanuts")[0]
    gluten_allergen = Allergen.objects.get_or_create(allergen_text="Gluten")[0]

    # Ajouter des ingrédients
    flour = Ingredient.objects.get_or_create(ingredient_text="Flour")[0]
    sugar = Ingredient.objects.get_or_create(ingredient_text="Sugar")[0]
    peanuts = Ingredient.objects.get_or_create(ingredient_text="Peanuts")[0]
    
    # Ajouter des allergènes à un ingrédient
    peanuts.ingredient_allergen_set.add(peanut_allergen)

    # Ajouter des étapes de recette
    step1 = RecipeStep.objects.get_or_create(step_text="Mix all dry ingredients")[0]
    step2 = RecipeStep.objects.get_or_create(step_text="Add wet ingredients and mix well")[0]
    step3 = RecipeStep.objects.get_or_create(step_text="Bake at 180°C for 25 minutes")[0]

    # Créer une recette
    recipe = Recipe.objects.get_or_create(
        recipe_title="Peanut Butter Cake",
        recipe_text="A delicious peanut butter cake recipe.",
        pub_date="2024-12-20",
    )[0]

    # Ajouter des ingrédients à la recette avec quantité, unité, et ordre
    RecipeIngredientLink.objects.get_or_create(
        recipe=recipe, ingredient=flour, order=1, quantity=200, unity=gram
    )
    RecipeIngredientLink.objects.get_or_create(
        recipe=recipe, ingredient=sugar, order=2, quantity=100, unity=gram
    )
    RecipeIngredientLink.objects.get_or_create(
        recipe=recipe, ingredient=peanuts, order=3, quantity=50, unity=gram
    )

    # Ajouter des étapes à la recette avec ordre
    RecipeStepOrder.objects.get_or_create(recipe=recipe, step=step1, order=1)
    RecipeStepOrder.objects.get_or_create(recipe=recipe, step=step2, order=2)
    RecipeStepOrder.objects.get_or_create(recipe=recipe, step=step3, order=3)

    print("Database populated successfully.")





def main():
    #Read file
    file = open('recipeList', 'r')
    url_list = file.readlines()
    for url in url_list:
        recipe = scrape_schema_recipe.scrape_url(url)
        Recipe.objects.get_or_create()


 
if __name__ == "__main__":
    populate_database()
    main()