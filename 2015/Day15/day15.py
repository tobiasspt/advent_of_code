#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import numpy as np
import re


def get_total_score(properties: np.ndarray) -> int:
    props = [x if x > 0 else 0 for x in properties[:-1]]
    score = 1
    for prop in props:
        score *= prop
    return score

## reading and parsing input
with open("input.txt", "r") as f:    
    A = f.read()
ingredients_raw = A.split("\n")
ingredients = []
for ingredient in ingredients_raw:
    numbers = re.findall(r"-?\d+", ingredient)
    ingredients.append(np.array([int(x) for x in numbers]))
    
max_tea_spoons = 100
total_scores = []
total_scores_500_calories = []
for i1 in range(max_tea_spoons+1):
    for i2 in range(max_tea_spoons+1-i1):
        for i3 in range(max_tea_spoons+1-i1-i2):
            if i1+i2+i3 > max_tea_spoons:
                continue
            i4 = max_tea_spoons - i1 - i2 - i3
            properties = i1 * ingredients[0] + i2 * ingredients[1] + i3 * ingredients[2] + i4 *ingredients[3]
            score = get_total_score(properties)
            total_scores.append(score)
            if properties[-1] == 500:
                total_scores_500_calories.append(score) 

res1 = max(total_scores)
print("Solution 1:", res1)
res2 = max(total_scores_500_calories)
print("Solution 2:", res2)



