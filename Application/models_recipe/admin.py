from django.contrib import admin

from .models import Recipe
from .models import Ingredient
from .models import Allergen
from .models import RecipeStep
from .models import RecipeIngredientLink
from .models import RecipeStepOrder
from .models import MesureUnity




admin.site.register(Ingredient)
admin.site.register(Allergen)
admin.site.register(RecipeStep)
admin.site.register(MesureUnity)



admin.site.site_header = "Recipe Admin"
#Add link between Recipe and RecipeIngredientOrder
class RecipeIngredientLinkInline(admin.TabularInline):
    model = RecipeIngredientLink
    extra = 1

#Add link between Recipe and RecipeStepOrder
class RecipeStepOrderInline(admin.TabularInline):
    model = RecipeStepOrder
    extra = 1

#add those to the Recipe admin page
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientLinkInline, RecipeStepOrderInline]