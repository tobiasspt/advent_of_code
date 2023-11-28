#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: tobias
"""

import numpy as np
with open("input.txt", "r") as f:    
    A = f.read()

flips = A.split()

def get_directions(flip):
    flipl = list(flip)
    directions_dict = {"e":0, "se":0, "ne":0, "w":0, "nw":0, "sw":0}
    i=0
    while i < len(flipl):

        c = flipl[i]
        try:
            cp1 = flipl[i+1]
        except: 
            cp1 = "x"
        
        if c == "e":
            directions_dict["e"] += 1
            i += 1
        elif c == "w":
            directions_dict["w"] += 1
            i += 1            
    
        elif c == "s":
            i += 2
            if cp1 == "w":
                directions_dict["sw"] += 1
            elif cp1 == "e":
                directions_dict["se"] += 1
                    
        elif c == "n":
            i += 2
            if cp1 == "w":
                directions_dict["nw"] += 1
            elif cp1 == "e":
                directions_dict["ne"] += 1
        
    return directions_dict
        

def get_xy_cords(directions_dict: dict) -> tuple[int]:
    sin60 = np.sqrt(3)/2
    cos60 = 1/2
    directions_table = {"e": np.array([ 1, 0]),
                       "w":  np.array([-1, 0]), 
                       "sw": np.array([-cos60, -sin60]), 
                       "nw": np.array([-cos60,  sin60]), 
                       "se": np.array([ cos60, -sin60]), 
                       "ne": np.array([ cos60,  sin60])}
    
    pos = np.zeros(2)
    for key in directions_dict.keys():
        pos += directions_table[key] * directions_dict[key]
    posx = round(pos[0]/cos60)
    posy = round(pos[1]/sin60)
    return tuple([posx, posy])


neighbour_dict = {}
def get_neighbours(pos: tuple[int]) -> list[tuple[int]]:
    
    if pos in neighbour_dict:
        return neighbour_dict[pos]
    else:
        x,y = pos
        neighbours = [(x+2, y), (x-2, y), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]
        neighbour_dict[pos] = neighbours
        return neighbours


#%% Part 1
black_tiles_set = set()
for flip in flips:
    tile_pos = get_xy_cords(get_directions(flip))
    if tile_pos not in black_tiles_set:
        black_tiles_set.add(tile_pos)
    else:
        black_tiles_set.remove(tile_pos)
        
solution1 = len(black_tiles_set)
print(f"Solution 1:\n{solution1}")

#%% Part 2
#starting from the flipped tiles from day 0

for i in range(1,101):

    possible_flips = set()
    possible_flips = possible_flips.union(black_tiles_set)
    
    for btile in black_tiles_set:
        neighbours = get_neighbours(btile)
        possible_flips = possible_flips.union(neighbours)
        
    new_black_tiles = set()
    
    for candidate in possible_flips:
        neighbouring_black_tiles = sum([1 for n in get_neighbours(candidate) if n in black_tiles_set])
        if candidate in black_tiles_set:
            if neighbouring_black_tiles in [1,2]:
                new_black_tiles.add(candidate)
        else:
            if neighbouring_black_tiles == 2:
                new_black_tiles.add(candidate)
                
    black_tiles_set = new_black_tiles
    print("Day", i, len(black_tiles_set))
print(f"Solution 2:\n{len(black_tiles_set)}")
    
        
 