import scrape_schema_recipe

class OtherRecipe:

    non_vegetarian_ingredients = ['Chicken','Beef','Pork','Fish','Lamb','Turkey','Duck','Goose','Crab','Shrimp','Lobster','Bacon','Sausage','Ham','Salmon','Tuna','Cod','Trout','Sardine','Mackerel','Anchovy','Herring','Mussel','Oyster','Clam','Octopus','Squid','Snail','Venison','Bison','Elk','Rabbit','Pheasant','Quail','Dove','Goat','Mutton','Horse','Kangaroo','Alligator','Frog','Turtle','Bear','Boar','Ostrich','Pigeon','Pheasant','Rattlesnake','Snail','Wild Boar','Wild Duck','Wild Turkey','Wild Goose','Wild Rabbit','Wild Pheasant','Wild Venison','Wild Elk','Wild Bison','Wild Boar','Wild Alligator','Wild Frog','Wild Turtle','Wild Bear','Wild Ostrich','Wild Pigeon','Wild Rattlesnake','Wild Snail','Wild Goose','Wild Rabbit','Wild Pheasant','Wild Venison','Wild Elk','Wild Bison','Wild Boar','Wild Alligator','Wild Frog','Wild Turtle','Wild Bear','Wild Ostrich','Wild Pigeon','Wild Rattlesnake','Wild Snail']
    def __init__(self, name, ingredients, instructions,image_link,cook_time,prep_time,difficulty):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.image_link = image_link
        self.cook_time = cook_time
        self.prep_time = prep_time
        self.difficulty = difficulty


    def get_ingredients(self):
        return self.ingredients
    
    def get_instructions(self):
        return self.instructions

    def contains(self, ingredient):
        return ingredient in self.ingredients
    
    def get_name(self):
        return self.name
    
    def is_vegetarian(self):
        return self.contains('meat') == False
    
    def get_allergens(self):
        allergens = []
        for ingredient in self.ingredients:
            if ingredient in Recipe.non_vegetarian_ingredients: #TODO: change to allergens
                allergens.append(ingredient)
        return allergens
    

    