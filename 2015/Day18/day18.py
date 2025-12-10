#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

from functools import lru_cache
from typing import Optional

def is_valid_neighbour(pos: tuple[int, int], map_size: int) -> bool:
    nx, ny = pos
    if nx < 0 or ny < 0 or nx >= map_size or ny >= map_size:
        return False
    return True

@lru_cache()
def get_neighbour_coords(pos: tuple[int,int], map_size: int) -> list[tuple[int,int]]:
    x, y = pos
    neighbours = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue
            neighbours.append((x+dx, y+dy))
    neighbours = [n   for n in neighbours if is_valid_neighbour(n, map_size)]
    return neighbours
        
def count_neighbour_active_lamps(map_list: list[list[str]], neighbours: list[tuple[int,int]]) -> int:
    active_lamps = 0
    for n in neighbours:
        nx, ny = n
        if map_list[ny][nx] == "#":
            active_lamps += 1
    return active_lamps

def count_all_acitve_lammps(map_list: list[list[str]]) -> int:
    active_lammps = sum(line.count("#") for line in map_list)
    return active_lammps


def evolve_n_times(n: int, map_list: list[list[str]], always_on_list: Optional[list[tuple[int,int]]]=[]) -> list[list[str]]:
    for i in range(n):
        new_map = []
        for y, line in enumerate(map_list):
            new_line = []
            for x, char in enumerate(line):
                n_active = count_neighbour_active_lamps(map_list, get_neighbour_coords((x,y), len(map_list)))
                if (x,y) in always_on_list: 
                    new_line.append("#")
                elif n_active == 3:
                    new_line.append("#")
                elif n_active == 2 and char == "#":
                    new_line.append("#")
                else:
                    new_line.append(".")
            new_map.append(new_line)
        map_list = new_map
    return map_list        


## Reading and parsing_input
with open("input.txt", "r") as f:    
    A = f.read()
map_list_start = [list(line) for line in A.split("\n")]

## Part 1
map_list_1 = evolve_n_times(100, map_list_start)
print("Solution 1:", count_all_acitve_lammps(map_list_1))

## Part 2
map_len = len(map_list_start)
always_on_list = [(0,0), (0, map_len-1), (map_len-1, 0), (map_len-1, map_len-1)]
map_list_2 = evolve_n_times(100, map_list_start, always_on_list)
print("Solution 2:", count_all_acitve_lammps(map_list_2))

