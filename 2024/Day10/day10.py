#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""


def get_neighbours(pos: tuple[int,int], size: tuple[int,int]) -> list[tuple[int,int]]:
    mx, my = size
    x, y = pos
    
    neighs = []
    if x > 0:
        neighs.append((x-1,y))
    if x < my-1:
        neighs.append((x+1,y))
    if y > 0:
        neighs.append((x,y-1))
    if y < my-1:
        neighs.append((x,y+1))    
        
    return neighs


def go_to_next_hight(ch: int, pos: list[int,int], hill_map: list[list[int]], peaks_found: list[tuple[int,int]]) -> list[tuple[int,int]]:
    size = (len(hill_map), len(hill_map[0]))
    
    if ch == 9: # we are on top
        return peaks_found + [pos]
        
    x,y = pos
    neighs = get_neighbours(pos, size)
    for n in neighs:
        nx,ny = n
        if hill_map[nx][ny] == ch + 1:
            peaks_found =  go_to_next_hight(ch+1, n, hill_map, peaks_found)
    return peaks_found 


def go_to_next_hight_2(ch: int, pos: list[int,int], hill_map: list[list[int]], path: str, unique_paths: int) ->int:
    size = (len(hill_map), len(hill_map[0]))
    
    path += str(pos)
    size = (len(hill_map), len(hill_map[0]))
    
    if ch == 9:
        return  unique_paths + 1
    x,y = pos
    neighs = get_neighbours(pos, size)
    for n in neighs:
        nx,ny = n
        if hill_map[nx][ny] == ch + 1:
            unique_paths = go_to_next_hight_2(ch+1, n, hill_map, unique_paths, path)
    return unique_paths


#%%

with open("input.txt", "r") as f:    
    A = f.read()
hill_map = [[int(x) for x in list(line)] for line in A.split("\n")]


## part 1
ratings = []
for x in range(len(hill_map)):    
    for y in range(len(hill_map[0])):
        if hill_map[x][y] == 0:
            peaks_found = go_to_next_hight(0, (x,y), hill_map, [])
            peaks_found = set(peaks_found)
            ratings.append(len(peaks_found))

total_ratings_1 = sum(ratings)
print("Solution 1:", total_ratings_1)


# part 2
ratings = []
for x in range(len(hill_map)):
    for y in range(len(hill_map[0])):
        if hill_map[x][y] == 0:
            rating = go_to_next_hight_2(0, (x,y), hill_map, 0)
            ratings.append(rating)
total_ratings = sum(ratings)
print("Solution 2:", total_ratings)

