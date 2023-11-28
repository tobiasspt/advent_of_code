#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

with open("input.txt", "r") as f:    
    A = f.read()
rules = A.split("\n")


# Part one
colors = [" ".join(rule.split('contain')[0].split()[:2]) for rule in rules]

parent_dict = {}
for c in colors:
    parent_dict[c] = []

for rule in rules:
    
    words = rule.split('contain')
    color = " ".join(words[0].split()[:2])
    can_contain = []
    numbers = []
    if "no other" in rule:
        1==1
    else:
        for bag in words[1].split(','):
            bag = bag.split()
            number = int(bag[0])
            color_cont = " ".join(bag[1:3])
            can_contain.append(color_cont)
            numbers.append(number)
    
    for c in can_contain:
        parent_dict[c].append(color)


parents_test = parent_dict["shiny gold"].copy()
parents_set = set(parents_test)
counter = 1

while len(parents_test) > 0:
    current = parents_test[0]
    current_list = parent_dict[current].copy()
    parents_test += current_list
    parents_set.add(current)
    parents_test.remove(current)
    counter += 1

print(f"Solution 1:\n{len(parents_set)}")

#%% Part two

def decode_rule(rule:str) -> (str, list[str], list[int]):
    words = rule.split('contain')
    color = " ".join(words[0].split()[:2])
    
    can_contain = []
    numbers = []
    if "no other" in rule:
        1==1
    else:
        for bag in words[1].split(','):
            bag = bag.split()
            number = int(bag[0])
            color_cont = " ".join(bag[1:3])
            can_contain.append(color_cont)
            numbers.append(number)
            
    return color, can_contain, numbers

dict_c = {}
for rule in rules:
    color, can_contain, numbers = decode_rule(rule)
    dict_c[color]= {}
    for can, num in zip(can_contain, numbers):
        dict_c[color][can] = num
    

def count_bags_in_bag(bag:str, factor:int) -> int:
    """
    This function is recursive
    """
    number_bags = factor
    for child, child_factor in dict_c[bag].items():
        number_bags += factor * count_bags_in_bag(child, child_factor)
    return number_bags
res = count_bags_in_bag("shiny gold", 1)
print(f"Solution 2:\n{res-1}")  #-1 as we do not count the shiny gold bag



    
    