#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import sys
sys.setrecursionlimit(30000)

def get_neighbours(pos: tuple[int,int], size: int, dist: int=1) -> list[tuple[int,int]]:
    x,y = pos
    sx, sy = size
    neighs = []
    if x >= dist:
        neighs.append((x-dist,y))
    if x < sx-dist:
        neighs.append((x+dist,y))
    if y >= dist:
        neighs.append((x, y-dist))
    if y < sy -dist:
        neighs.append((x, y+dist))
    return neighs

pos_dict = {}
def move_one_step(pos: tuple[int,int], step: int, area: list[list[str]]) -> None:
    ## Recursive functions
    if pos not in pos_dict.keys():
        pos_dict[pos] = step
    neighs = get_neighbours(pos, (1e10,1e10))
    neighs = [n for n in neighs if area[n[1]][n[0]] !="#"]
    for n in neighs:
        if n not in pos_dict:
            move_one_step(n, step+1, area)
            
def get_tiles_within_distance(pos: tuple[int,int], max_distance: int, size: tuple[int,int]) -> tuple[list[tuple[int,int]], list[int]]:
    px, py = pos
    sx, sy = size
    xy_candidates = []
    xy_distances = []
    
    for x in range(-max_distance, max_distance+1):
        for y in range(-max_distance, max_distance+1):
            distance = abs(x)+abs(y)
            if 2 <= distance <= max_distance:
                xy_candidates.append((px+x, py+y))
                xy_distances.append(distance)
    neighs = []
    n_dist = []
    for n, d in zip(xy_candidates, xy_distances):
        nx, ny = n 
        if 0 <= nx <= sx-1:
            if 0 <= ny <= sy-1:
                neighs.append(n)
                n_dist.append(d)
    return neighs, n_dist

def naming(pos_list: list[tuple[int,int], tuple[int,int]]) -> str:
    pos_list = sorted(pos_list)
    p1, p2 = pos_list
    return str(p1[0])+","+str(p1[1])+","+str(p2[0])+","+str(p2[1])


    
## Reading and parsing input
with open("input.txt", "r") as f:    
    A = f.read()
area = [list(line) for line in A.split("\n")]
for y, line in enumerate(area):
    for x, char in enumerate(line):
        if char == "S":
            start = (x,y)
        elif char == "E":
            end = (x,y)
size = (len(area), len(area[0]))
 
## Calculate all the distances from the start
move_one_step(start, 0, area)
    
## part 1
all_cheat_benefits = []
for pos in pos_dict.keys():
    two_step_neighs = get_neighbours(pos, size, dist=2)
    two_step_neighs = [n for n in two_step_neighs if area[n[1]][n[0]] !="#"]
    for n in two_step_neighs:
        cheat_benefit =   pos_dict[pos] - pos_dict[n] - 2
        if cheat_benefit > 0:
            all_cheat_benefits.append(cheat_benefit)
res1 = sum([x>=100 for x in all_cheat_benefits]) 
print("Solution 1:", res1)   
    
## part 2, cheats may last up to 20 ps!
## part 1 can also be solved with the code of part 2
distance = 20
cheats_dict = {}
for ii, pos in enumerate(pos_dict):
    _neighs, _n_dist = get_tiles_within_distance(pos, distance, size)
    neighs = []
    n_dist = []
    for n, d in zip(_neighs, _n_dist):
        if area[n[1]][n[0]] !="#":
            neighs.append(n)
            n_dist.append(d)
    
    for n,d in zip(neighs, n_dist):
        name = naming([pos, n])
        if name not in cheats_dict.keys():
            cheat_benefit =   pos_dict[pos] - pos_dict[n] - d
            if cheat_benefit > 0:
               cheats_dict[name] = cheat_benefit

res2 = sum([x>=100 for x in cheats_dict.values()]) 
print("Solution 2:", res2)


    