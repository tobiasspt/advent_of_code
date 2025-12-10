#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

from itertools import permutations

### Recycling of day 9 functions. Only difference is that the start and end
### have a connection too. 

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
    dist += dist_dict[locations[-1]][locations[0]]
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
    
def get_pairs(couples: list[str]) -> list[list[str, str, int]]:
    pairs_dict = dict()
    for couple in couples:
        words = couple.split()
        p1 = words[0]
        p2 = words[-1][:-1]
        value = int(words[3])
        if words[2] == "lose":
            value = -value
        key = tuple(sorted([p1,p2]))
        if key in pairs_dict.keys():
            pairs_dict[key] += value
        else:
            pairs_dict[key] = value
    pairs = [[key[0], key[1], value] for key, value in pairs_dict.items()]
    return pairs    

## Reading input
with open("input.txt", "r") as f:    
    A = f.read()
couples_raw = A.split("\n")

## part 1
pairs = get_pairs(couples_raw)
all_distances_list = get_all_distances(pairs)
res1 = max(all_distances_list)
print("Solution 1:", res1)

## part 2, adding myself
all_people = set([p[0] for p in pairs] + [p[1] for p in pairs])
pairs2 = pairs.copy()
for person in all_people:
    pairs2.append(["ego", person, 0])
all_distances_list_2 = get_all_distances(pairs2)
res2 = max(all_distances_list_2)
print("Solution 2:", res2)


