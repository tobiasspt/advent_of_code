#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: tobias
"""

import matplotlib.pyplot as plt
import numpy as np
import copy
import time

with open("input.txt", "r") as f:    
    A = f.read()
    


def is_valid_arrangement(springs:str, groups):
    groups_now = [len(y) for y in [x for x in springs.split(".") if x != ""]]
    return groups_now == groups


def springs_can_be_valid(springs, groups):
    num_defect_total = sum(groups)
    num_defect_known = springs.count("#")
    num_defect_extra = springs.count("?")
    
    if num_defect_known <= num_defect_total <= num_defect_known + num_defect_extra:
        return True
    else:
        return False
    
    
    
def clean_known_part(springs, groups):
    
    springs = springs.strip('.')
    
    if not springs_can_be_valid(springs, groups):
        return False, None, None
    
    springs_len = len(springs)
    
    
    # No more unknowns inside
    if springs.count("?") == 0:
        valid_bool = is_valid_arrangement(springs, groups)
        if valid_bool:
            return True, "", []
        else:
            return False, None, None
    

    while springs[0] == "#":

        group_len = groups[0]
        part = springs[:group_len]
        
        if group_len != len(springs) and springs[group_len] == "#":
            return False, None, None
        
        if "." in part:
            return False, None, None
        else:
            springs = springs[group_len+1:]
            springs = springs.strip('.')
            groups = groups[1:]
            
        springs_len = len(springs)
        if springs_len == 0 and sum(groups) == 0:
            return True, "", []
        if springs_len == 0 and sum(groups) > 0:
            return False, None, None
        if not springs_can_be_valid(springs, groups):
            return False, None, None
        
    if springs_len == 0 and sum(groups) > 0:
        return False, None, None
        
    return True, springs, groups



def replace_one_unknown(springs):
    
    indexes = np.where(np.array(list(springs)) == "?")[0] 
    string_lists = [springs.replace("?", ".")]

    for i in indexes:
        
        foo = springs[:i]
        foo = foo.replace("?", ".")
        
        s = foo + "#" + springs[i+1:]
        string_lists.append(s)
        
    return string_lists


"""
My onw approach to memoization / caching
"""
def generate_hash(springs, groups):
    return springs + str(groups)
dict_of_doom = {}


def count_arrangements(springs, groups):
    counter = 0
    
    # Remove the known part, once at the front and once at the back
    can_valid, springs, groups = clean_known_part(springs, groups)
    if not can_valid:
        return counter
    if springs != '':
        can_valid, springs, groups = clean_known_part(springs[::-1], groups[::-1])
        if not can_valid:
            return counter
        else:
            springs = springs[::-1]
            groups = groups[::-1]
    
    
    # My own implementation of memoization. Could be done using functools.cache
    doom_hash = generate_hash(springs, groups)
    if doom_hash in dict_of_doom:
        return dict_of_doom[doom_hash]
    
    
    # The arrangment was valid: 
    if sum(groups) == 0 and springs.count("#") == 0:
        dict_of_doom[doom_hash] = counter +1
        return counter + 1
    
    
    # After the removement of the known part, the springs string does start with a "?"
    # Get the possible next states of when one "?" is replaced with a "." or "#"
    possible_next = replace_one_unknown(springs)
    for next_springs in possible_next:
        counter  += count_arrangements(next_springs, groups)

    dict_of_doom[doom_hash] = counter 
    return counter



# Read and parse the input
spring_rows = A.split("\n")
row_dict = {}

### Part 1
factor = 1
for i, row in enumerate(spring_rows):
    springs, groups = row.split()
    groups = [int(x) for x in groups.split(",")]
    springs_string = "?".join([springs]*factor)
    springs_string.strip(".")
    row_dict[i] = {"sp":springs_string, "gr":groups*factor}
    
nums = []
for row in row_dict.keys():
    springs = row_dict[row]["sp"]
    groups = row_dict[row]["gr"]
    nums.append(count_arrangements(springs, groups))
res1 = sum(nums)
print(f"Solution 1\n{res1}")


### Part 2
to = time.time()
factor = 5
for i, row in enumerate(spring_rows):
    springs, groups = row.split()
    groups = [int(x) for x in groups.split(",")]
    springs_string = "?".join([springs]*factor)
    springs_string.strip(".")
    row_dict[i] = {"sp":springs_string, "gr":groups*factor}
    
nums2 = []
for row in row_dict.keys():
    springs = row_dict[row]["sp"]
    groups = row_dict[row]["gr"]
    nums2.append(count_arrangements(springs, groups))
res2 = sum(nums2)
print(f"Solution 1\n{res2}")

print(time.time()-to)

