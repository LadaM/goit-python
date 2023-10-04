import os

def get_recipe(path, search_id):
    recipe = None

    with open(path, 'r') as file:
        for line in file.readlines():
            id, name, *ingredients = line.strip('\n').split(',')
            if id == search_id:
                recipe = {
                    "id": id,
                    "name": name,
                    "ingredients": ingredients
                }
                print(recipe)
                return recipe

absolute_path = os.path.dirname(__file__) # getcwd() doesn't give the correct location of this file because working dir is the whole repo
relative_path = 'recipes.txt'
path = os.path.join(absolute_path, relative_path)

get_recipe(path=path, search_id='60b90c1c13067a15887e1ae0')


