#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
"Travelling salesmen, except not comming back to start."

from itertools import permutations

def get_pair(pair: str) -> tuple[int,int,int]:
    words = pair.split()
    dist = int(words[-1])
    loc1 = words[0]
    loc2 = words[2]
    return (loc1, loc2, dist)

def calculate_distance_dict(pairs: list[str, str, int]) -> dict:
    all_locs = set([p[0] for p in pairs] + [p[1] for p in pairs])
    dist_dict = {}
    for loc in all_locs:
        dist_dict[loc] = {}
    for loc1, loc2, dist in pairs:
        dist_dict[loc1][loc2] = dist
        dist_dict[loc2][loc1] = dist
    return dist_dict
    
def calc_distance(locations: list[str], dist_dict: dict) -> int:
    dist = 0
    for i in range(len(locations)-1):
        dist += dist_dict[locations[i]][locations[i+1]]
    return dist
        
def get_all_distances(pairs: list[tuple[int,int,int]]) -> list[int]:
    dist_dict = calculate_distance_dict(pairs)
    all_locs = set(dist_dict.keys())    
    
    all_distances_list = []
    for loc1, loc2, dist in pairs:
        middle_set = all_locs - {loc1, loc2}
        perms = permutations(middle_set)
        all_distances = [calc_distance([loc1]+list(perm)+[loc2], dist_dict) for perm in perms]
        all_distances_list += all_distances
    
    return all_distances_list
    

## Reading input
with open("input.txt", "r") as f:    
    A = f.read()
pairs_raw = A.split("\n")

## Calculating all distances
pairs = [get_pair(pair) for pair in pairs_raw]
all_distances_list = get_all_distances(pairs)

res1 = min(all_distances_list)
print("Solution 1:", res1)
res2 = max(all_distances_list)
print("Solution 2:", res2)
