# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""

from functools import lru_cache
import itertools


@lru_cache
def get_neigbours(coords:  tuple[int, int], map_string:str) -> list[tuple[int, int]]:
    
    map_list = [list(x) for x in map_string.split("\n")]
    x,y = coords
    neighbours = []
    #dont need to bother about -1 indices, as all outer tiles are walls
    if map_list[x-1][y] != '#':
        neighbours.append((x-1, y))
    if map_list[x+1][y] != '#':
        neighbours.append((x+1, y))
    if map_list[x][y+1] != '#':
        neighbours.append((x, y+1))
    if map_list[x][y-1] != '#':
        neighbours.append((x, y-1))
        
    return neighbours
    

def flood_area(start: tuple[int, int], targets: list[tuple[int,int]], map_string: str) -> dict:
    
    reached_in_dict = {}
    already_flooded = set()
    already_flooded.add(start)
    currently_flooded = set(get_neigbours(start, map_string))
    steps = 1
    
    while len(currently_flooded) > 0:
        already_flooded = already_flooded.union(currently_flooded)
        new_flooded = set()
        for cf in currently_flooded:
 
            if cf in targets:
                reached_in_dict[cf] = steps
                
            n_neighs = get_neigbours(cf, map_string)
            for nn in n_neighs:
                if nn in already_flooded:
                    continue
                else:
                    new_flooded.add(nn)
                    
        steps += 1
        currently_flooded = new_flooded

    return reached_in_dict


def length(permutation: tuple[tuple[int,int]]) -> int:
    l = 0
    l += target_dict[start]["steps_to"][permutation[0]]
    for i, p in enumerate(permutation[:-1]):
        l += target_dict[p]["steps_to"][permutation[i+1]]
    return l


def length_2(permutation: tuple[tuple[int,int]]) -> int:
    l = 0
    l += target_dict[start]["steps_to"][permutation[0]]
    for i, p in enumerate(permutation[:-1]):
        l += target_dict[p]["steps_to"][permutation[i+1]]
    l += target_dict[permutation[-1]]["steps_to"][start]
    return l


#%%
#Reading the input
with open('input.txt','r') as f:    
    map_string = f.read()
    
map_list = [list(x) for x in map_string.split("\n")]
    

target_dict = {}
for target in [str(a) for a in range(8)]:
    for x in range(len(map_list)):
        for y in range(len(map_list[x])):
            if map_list[x][y] == target:
                target_dict[(x,y)] = {"name":target}
                if target == "0":
                    start = (x,y)
    
### finding the shortest way from a starting point to each number (target)
for target in target_dict.keys():
    reach_in_dict = flood_area(target, list(target_dict.keys()), map_string)
    target_dict[target]["steps_to"] = reach_in_dict
    

targets = [x for x in target_dict.keys()]
targets.remove(start)
all_permutations = set(itertools.permutations(targets))


#part1
solution1 = min([length(p) for p in all_permutations])
print("Solution 1", solution1)

#part2
solution2 = min([length_2(p) for p in all_permutations])
print("Solution 2", solution2)
    

    
    
    