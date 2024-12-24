from django.db import models



class Recipe(models.Model):
    recipe_title = models.CharField(max_length=200)
    recipe_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    recipe_ingredients = models.ManyToManyField('Ingredient', through='RecipeIngredientLink')
    recipe_steps = models.ManyToManyField('RecipeStep', through='RecipeStepOrder')

    def __str__(self):
        return self.recipe_text
    
    def get_ingredients(self):
        #Put the ingredients in order
        ingredients = self.recipe_ingredients.all().order_by('recipeingredientlink__order')
        returnTuple = []
        for ingredient in ingredients:
            qty = self.get_quantity(ingredient.id)
            unity = self.get_unity(ingredient.id)
            returnTuple.append((ingredient, qty, unity))
        yield from (ingredient for ingredient in returnTuple)
    
    def get_quantity(self, ingredient_id):
        #Get the quantity of an ingredient
        quantity = self.recipe_ingredients.get(pk=ingredient_id).recipeingredientlink_set.all()[0].quantity
        return quantity
    
    def get_unity(self, ingredient_id):
        #Get the unity of an ingredient
        unity = self.recipe_ingredients.get(pk=ingredient_id).recipeingredientlink_set.all()[0].unity
        return unity

    def get_steps(self):
        #Put the steps in order
        steps = self.recipe_steps.all().order_by('recipesteporder__order')
        yield from (step for step in steps)

    def get_allergens(self):
        #Get all the allergens of the recipe
        allergens = []
        for ingredient in self.recipe_ingredients.all():
            for allergen in ingredient.ingredient_allergen_set.all():
                allergens.append(allergen)
        return allergens

class Ingredient(models.Model):
    ingredient_text = models.CharField(max_length=200)
    ingredient_allergen_set = models.ManyToManyField('Allergen', blank=True)

    def __str__(self):
        return self.ingredient_text

class RecipeIngredientLink(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    unity = models.ForeignKey('MesureUnity', on_delete=models.CASCADE)

class Allergen(models.Model):
    allergen_text = models.CharField(max_length=200)

    def __str__(self):
        return self.allergen_text

class RecipeStep(models.Model):
    step_text = models.CharField(max_length=200)

    def __str__(self):
        return self.step_text

class RecipeStepOrder(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step = models.ForeignKey(RecipeStep, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

class MesureUnity(models.Model):
    unity_text = models.CharField(max_length=200)

    def __str__(self):
        return self.unity_text
