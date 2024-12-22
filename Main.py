from Recipe import Recipe
from database_connector import DatabaseConnector

def main():
    server = ""
    #connect to databae
    connection = DatabaseConnector(server=server, database="postgres", username="postgres", password="RiHU<6iNVk`bn6vr")

    #Read file
    file = open('recipeList', 'r')
    url_list = file.readlines()
    recipes = []
    for url in url_list:
        recipes.append(Recipe.get_recipe_from_url(url))

    for recipe in recipes:
        print(recipe.get_name())


 

main()