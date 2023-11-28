#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: tobias
"""

from collections import defaultdict, Counter


with open("input.txt", "r") as f:    
    A = f.read()

"""
Each line one food
contains ingredients and some or all alergenes
each alergen in EXACTLY one ingredient
each ingredient contains 0 or 1 alergen
"""

recipes = A.split("\n")

# Dictionary where every alergene is a key
alergenes_dict = defaultdict(lambda: {"ingredents_lists":[], "possible_ingredients":[]})
recipes_dict = {}

# Reading the recipies, creating an alergene dict
for i, recipe in enumerate(recipes):
    ingredients, alergenes = recipe.split("(contains")
    ingredients = ingredients.split()
    ingredients = [ing.strip() for ing in ingredients]
    alergenes_list = alergenes.strip(")").split(',')
    alergenes_list = [al.strip() for al in alergenes_list]
    recipes_dict[i] = ingredients
    for al in alergenes_list:
        alergenes_dict[al]["ingredents_lists"].append(ingredients)
    
    
# Going over the alergenes and finding out to which ingredients they possibly belong to
for al in alergenes_dict.keys():
    number_recipies = len(alergenes_dict[al]["ingredents_lists"])
    all_ingredients = [ingredient for sublist in alergenes_dict[al]["ingredents_lists"] for ingredient in sublist]
    ingredient_counter = Counter(all_ingredients)
    for ingredient in ingredient_counter:
        if ingredient_counter[ingredient] == number_recipies:
            alergenes_dict[al]["possible_ingredients"].append(ingredient)
    
    
# Finding out which is the right ingredient belonging to an alergene. 
# Done by identifying the first aleregene which has only one possible ingredient. 
# Thene remove this one from all others if its there. Then go on like this. 
alergenes_to_check = list(alergenes_dict.keys())    

for i in range(9):
    for al in alergenes_to_check:
        if len(alergenes_dict[al]["possible_ingredients"]) == 1:
            only_ingredient = alergenes_dict[al]["possible_ingredients"][0]
            alergenes_to_check.remove(al)
            for al2 in alergenes_to_check:
                if only_ingredient in  alergenes_dict[al2]["possible_ingredients"]:
                    alergenes_dict[al2]["possible_ingredients"].remove(only_ingredient)
            break
        

ingredients_with_alergenes  = [alergenes_dict[al]["possible_ingredients"][0] for al in alergenes_dict.keys()]
all_ingredients_all_recipes = [ing for recipe in recipes_dict.values() for ing in recipe ]
all_ingredients_counter = Counter(all_ingredients_all_recipes)
solution1 = sum([all_ingredients_counter[ing] for ing in all_ingredients_counter.keys() if ing not in ingredients_with_alergenes])
print(f"Solution 1:\n{solution1}")
    
#%% Part 2
alergenes = list(alergenes_dict.keys())
alergenes.sort()
toxic_ingredients = [alergenes_dict[al]["possible_ingredients"][0] for al in alergenes]
solution2 = ",".join(toxic_ingredients)
print(f"Solution 2\n{solution2}")
    