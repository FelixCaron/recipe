from django.http import HttpResponse
from .models import Recipe
from django.template import loader
from django.shortcuts import render
from django.http import Http404


def index(request):
    all_recipe = Recipe.objects.order_by("-pub_date")[:5]
    
    context = {
        "all_recipe": all_recipe,
    }
    return render(request, "recipe/index.html", context)

def detail(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return render(request, "recipe/detail.html", {"recipe": recipe})


