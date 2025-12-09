#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: tobias
"""

def is_in_range(ingredient_id: int, id_range: tuple[int,int]) -> bool:
    x,y = id_range
    return x <= ingredient_id <= y
    

def is_fresh(ingredient_id: int, ranges: list[tuple[int,int]]) -> bool:
    fresh = False
    for id_range in ranges:
        if is_in_range(ingredient_id, id_range):
            fresh = True
            break
    return fresh


def have_overlap(range1: tuple[int,int], range2: tuple[int,int]):
    "Assumption that range 1 has always lower start"
    x1,y1 = range1
    x2,y2 = range2
    if y1 >= x2:
        return True
    else:
        return False
    

def get_common_range(range1: tuple[int,int], range2: tuple[int,int]):
    "Assumption that range 1 has always lower start"
    x1,y1 = range1
    x2,y2 = range2
    return (x1, max(y1,y2))
    

def merge_ranges(ranges: list[tuple[int,int]]) -> list[tuple[int,int]]:
    sorted_ranges  = sorted(ranges)
    
    changed = True
    while changed:
        changed = False
        
        new_ranges = []
        for i in range(len(sorted_ranges)-1):
            r1 = sorted_ranges[i]
            r2 = sorted_ranges[i+1]
        
            if have_overlap(r1, r2):
                nr = get_common_range(r1, r2)
                new_ranges.append(nr)
                changed = True
                new_ranges += sorted_ranges[i+2:]
                sorted_ranges = new_ranges

                break
            
            new_ranges.append(r1)
        sorted_ranges = new_ranges
    new_ranges.append(r2)
    return new_ranges



## Reading and parsing input
with open("input.txt", "r") as f:    
    A = f.read()
ranges, ingredients = A.split("\n\n")
ranges = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in ranges.split("\n") ]
ingredients = list(map(int, ingredients.split("\n")))


## Part 1
res1 = sum([is_fresh(x, ranges) for x in ingredients])
print(f"Solution 1: {res1}")


##  Part 2
merged_ranges = merge_ranges(ranges)
res2 = sum([x[1]-x[0] + 1 for x in merged_ranges])
print(f"Solution 2: {res2}")
            
    
    
    
    
    