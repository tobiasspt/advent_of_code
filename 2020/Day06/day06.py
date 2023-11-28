#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: tobias
"""


import numpy as np


with open("input.txt", "r") as f:    
    A = f.read()

# A = """abc

# a
# b
# c

# ab
# ac

# a
# a
# a
# a

# b"""    
 
    

groups = A.split("\n\n")
    
    
#part one
def count_anyone(group):
    persons = group.split("\n")
    all_answers = []
    for person in persons:
        all_answers+=list(person)
    return len(np.unique(all_answers))

solution1 = sum([count_anyone(group) for group in groups])

print(f"Solution 1:\n{solution1}")


#%% part two

from collections import Counter

def count_all(group):
    persons = group.split("\n")
    number_persons = len(persons)
    all_answers = []
    for person in persons:
        all_answers+=list(person)
    counter = Counter(all_answers)
    
    all_yes = 0
    for key in counter:
        if counter[key]==number_persons:
            all_yes += 1
        
    return all_yes

solution2 = sum([count_all(group) for group in groups])

print(f"Solution 2:\n{solution2}")


