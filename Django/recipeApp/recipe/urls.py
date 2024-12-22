from django.urls import path

from . import views

app_name = "recipe"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:recipe_id>/", views.detail, name="detail"),

]