#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
Takes ~ 3min. But I am fine with it ;)
"""

import copy


with open("input.txt", "r") as f:    
    A = f.read()

map_list = [list(line) for line in A.split()]
xlen = len(map_list)
ylen = len(map_list[0])


def find_neighbours(pos: tuple[int,int]) -> list[tuple[int, int]]:
    x,y = pos
    
    if map_list[x][y] in ["<", ">", "v"]:
        ind = ["<", ">", "v"].index(map_list[x][y])
        next_pos = [(x,y-1), (x,y+1), (x+1,y)][ind]
        return [next_pos]
        
    neighs = [(x-1,y), (x+1,y), (x, y-1), (x, y+1)]
    neighs = [pos for pos in neighs if pos[0] >= 0 and pos[0] < xlen]
    neighs = [pos for pos in neighs if pos[0] >= 0 and pos[0] < xlen]
    neighs = [pos for pos in neighs if map_list[pos[0]][pos[1]] != "#"]
    return neighs


def find_neighbours_2(pos: tuple[int,int]) -> list[tuple[int, int]]:
    x,y = pos
    
    neighs = [(x-1,y), (x+1,y), (x, y-1), (x, y+1)]
    neighs = [pos for pos in neighs if pos[0] >= 0 and pos[0] < xlen]
    neighs = [pos for pos in neighs if pos[0] >= 0 and pos[0] < xlen]
    neighs = [pos for pos in neighs if map_list[pos[0]][pos[1]] != "#"]
    return neighs



### Making a dictionary containing all the crossings and the corresponding 
### connected crossings
crossing_dict = dict()

for x in range(len(map_list)):
    for y in range(len(map_list[0])):
        
        if map_list[x][y] == "#":
            continue
        
        neighs = [(x-1,y), (x+1,y), (x, y-1), (x, y+1)]
        neighs = [pos for pos in neighs if pos[0] >= 0 and pos[0] < xlen]
        neighs = [pos for pos in neighs if pos[1] >= 0 and pos[1] < ylen]
        
        symbols = [map_list[p[0]][p[1]] for p in neighs]
        symbols = [sym for sym in symbols if sym != "#"]
        
        if len(symbols) >= 3:
            crossing_dict[(x,y)] = {"neighbours":[], "steps":[]}
crossing_dict[(0,1)] = {"neighbours":[], "steps":[]}
crossing_dict[(xlen-1, ylen-2)] = {"neighbours":[], "steps":[]}



def find_next_crossing(start: tuple[int, int], neigh: list[tuple[int, int]]) -> (tuple[int, int], int):
    
    pos_to_check = [[neigh, start, 0]]
    
    while len(pos_to_check) > 0:
        pos, last, steps_walked = pos_to_check[0]
        del pos_to_check[0]
        
        if pos in crossing_dict:
            return pos, steps_walked
        
        neighs = find_neighbours_2(pos)
        neighs = [p for p in neighs if p != last]

        for n in neighs:
            pos_to_check.append( [n, pos, steps_walked+1])


for crossing in crossing_dict:
    neighs = find_neighbours_2(crossing)
    for n in neighs:
        next_crossing, steps = find_next_crossing(crossing, n)
        crossing_dict[crossing]["neighbours"].append(next_crossing)
        crossing_dict[crossing]["steps"].append(steps+1)
###


#%% Part 1

pos_to_check = [[(0,1),(-1,0), 0]]

arrivals_steps = []
while len(pos_to_check) > 0:
    pos, last, steps_walked = pos_to_check[0]
    del pos_to_check[0]
    if pos[0] == xlen -1 and pos[1] == ylen -1-1:
        arrivals_steps.append(steps_walked)
        continue
    
    neighs = find_neighbours(pos)
    neighs = [p for p in neighs if p != last]
    
    for n in neighs:
        pos_to_check.append( [n, pos, steps_walked+1])


res1 = max(arrivals_steps)
print(f"Solution 1\n{res1}")


#%% Part 2

def check_next(pos_to_check: tuple[int, int], arrivals_steps_2)  -> None:
    
    pos,  steps_walked, traveresed_crossings = pos_to_check
    
    if pos == (xlen-1, ylen-2):
        arrivals_steps_2.append(steps_walked)
        return arrivals_steps_2
    
    if pos in traveresed_crossings:
        return arrivals_steps_2
    
    traveresed_crossings.append(pos)
    next_crossings  = crossing_dict[pos]["neighbours"]
    additional_steps = crossing_dict[pos]["steps"]
    
    for n, c in zip(next_crossings, additional_steps):    
        check_next([n, steps_walked+c, copy.copy(traveresed_crossings)], arrivals_steps_2)
    
    return arrivals_steps_2

import time

t0 = time.time()

arrivals_steps_2 = check_next([(0,1), 0, []], [])
print(time.time()-t0)

res2 = max(arrivals_steps_2)
print(f"Solution 2\n{res2}")






