#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: tobias
"""

from collections import defaultdict
from itertools import product
import copy

with open("input.txt", "r") as f:    
    A = f.read()

# A = """.#.
# ..#
# ###
# """

lines = A.split('\n')


neighbour_dict = defaultdict(lambda: None)

def get_neighbours(pos: tuple) -> list[tuple]:
    """
    Returns the set of possible neighbours in 3D
    Additionally fills the lookuptable -> neighbour_dict
    """
    x,y,z = pos
    if not neighbour_dict[pos]:
        neighbours = set()
        for xp, yp, zp in product(range(-1,2,1), range(-1,2,1), range(-1,2,1)):
            neighbours.add((x+xp,y+yp,z+zp))
        neighbours.remove(pos)
        neighbour_dict[pos] = neighbours
    else:
        neighbours = neighbour_dict[pos]  
    assert len(neighbours) == 3**3 - 1
    return neighbours
        
        
def get_all_neighbours(active_cubes):
    neighbour_cubes = set()
    for pos in active_cubes:
        neighs = get_neighbours(pos)
        neighbour_cubes = neighbour_cubes.union(neighs)
    
    return neighbour_cubes


def get_number_of_active_neighs(pos: set(), active_cubes: set(set())) -> int:
    neighbours = get_neighbours(pos)
    return sum([1 for x in neighbours if x in active_cubes])



active_cubes = set()
for x, line in enumerate(lines):
    for y, state in enumerate(line):
        if state == "#":
            active_cubes.add((x,y,0))

# Checking the cubes in cycles
all_neighbours = get_all_neighbours(active_cubes)
all_cubes_to_consider = all_neighbours.union(active_cubes)


cycles = 6
for i in range(cycles):
    
    all_neighbours = get_all_neighbours(active_cubes)
    all_cubes_to_consider = all_neighbours.union(active_cubes)
    new_active_cubes = set()
    
    for cube in all_cubes_to_consider:
        num_active_neighs = get_number_of_active_neighs(cube, active_cubes)
        if cube in active_cubes and num_active_neighs in [2,3]:
            new_active_cubes.add(cube)
        else:
            if num_active_neighs == 3:
                new_active_cubes.add(cube)
    active_cubes = copy.deepcopy(new_active_cubes)
        
solution1 = len(active_cubes)    
print(f"Solution 1:\n{solution1}")

#%% 4D

neighbour_dict_4d = defaultdict(lambda: None)

def get_neighbours_4d(pos: tuple) -> list[tuple]:
    """
    Returns the set of possible neighbours in 3D
    Additionally fills the lookuptable -> neighbour_dict
    """
    x,y,z,w = pos
    if not neighbour_dict_4d[pos]:
        neighbours = set()
        for xp, yp, zp, wp in product(range(-1,2,1), range(-1,2,1), range(-1,2,1), range(-1,2,1)):
            neighbours.add((x+xp,y+yp,z+zp, w+wp))
        neighbours.remove(pos)
        neighbour_dict_4d[pos] = neighbours
    else:
        neighbours = neighbour_dict_4d[pos]  
    assert len(neighbours) == 3**4 - 1
    return neighbours
        
        
def get_all_neighbours_4d(active_cubes):
    neighbour_cubes = set()
    for pos in active_cubes:
        neighs = get_neighbours_4d(pos)
        neighbour_cubes = neighbour_cubes.union(neighs)
    return neighbour_cubes


def get_number_of_active_neighs_4d(pos: set(), active_cubes: set(set())) -> int:
    neighbours = get_neighbours_4d(pos)
    return sum([1 for x in neighbours if x in active_cubes])



active_cubes_4d = set()
for x, line in enumerate(lines):
    for y, state in enumerate(line):
        if state == "#":
            active_cubes_4d.add((x,y,0,0))

# Checking the cubes in cycles
all_neighbours_4d = get_all_neighbours_4d(active_cubes_4d)
all_cubes_to_consider_4d = all_neighbours_4d.union(active_cubes_4d)


cycles = 6
for i in range(cycles):
    
    all_neighbours_4d = get_all_neighbours_4d(active_cubes_4d)
    all_cubes_to_consider_4d = all_neighbours_4d.union(active_cubes_4d)
    new_active_cubes_4d = set()
    
    for cube in all_cubes_to_consider_4d:
        num_active_neighs = get_number_of_active_neighs_4d(cube, active_cubes_4d)
        if cube in active_cubes_4d and num_active_neighs in [2,3]:
            new_active_cubes_4d.add(cube)
        else:
            if num_active_neighs == 3:
                new_active_cubes_4d.add(cube)
    active_cubes_4d = copy.deepcopy(new_active_cubes_4d)
        
solution2 = len(active_cubes_4d)    
print(f"Solution 1:\n{solution2}")

