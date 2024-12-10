#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""


def find_all_antinodes(antenna_pos: list[tuple[int,int]]) -> list[tuple[int,int]]:
    antinode_pos = []
    for i, p1 in enumerate(antenna_pos[:-1]):
        x1, y1 = p1
        for j, p2 in enumerate(antenna_pos[i+1:]):
            x2, y2 = p2
            diffx = x1-x2
            diffy = y1-y2
            antinode_pos += [(x1+diffx, y1+diffy), (x2-diffx, y2-diffy)]
    return antinode_pos

def is_valid_pos(pos: tuple[int,int], size: list[int,int]) -> bool:
    maxy, maxx = size
    x,y = pos
    if x < 0 or x >= maxx or y < 0 or y >= maxy:
        return False
    else:
        return True
  
def get_resonant_harmonics(p1: tuple[int,int], p2: tuple[int,int], size: list[int,int]) -> list[tuple[int,int]]:
    x1, y1 = p1
    x2, y2 = p2
    diffx = x1-x2
    diffy = y1-y2
    antinode_pos = []
    
    n1 = 0
    while True:
        ap = (x1+n1*diffx, y1+n1*diffy)
        if is_valid_pos(ap, size):
            antinode_pos.append(ap)
            n1+=1
        else:
            break
    n1 = 0
    while True:
        ap = (x2-n1*diffx, y2-n1*diffy)
        if is_valid_pos(ap, size):
            antinode_pos.append(ap)
            n1+=1
        else:
            break
    return antinode_pos 

def find_all_antinodes_2(antenna_pos: list[tuple[int,int]], size: list[int,int]) -> list[tuple[int,int]]:
    antinode_pos = []
    for i, p1 in enumerate(antenna_pos[:-1]):
        for j, p2 in enumerate(antenna_pos[i+1:]):
            antinode_pos += get_resonant_harmonics(p1, p2, size)
    return antinode_pos
        
    
###  input parsing
with open("input.txt", "r") as f:    
    A = f.read()
roof = [list(x) for x in A.split()]
antenna_dict = {}
for y, line in enumerate(roof):
    for x, l in enumerate(line):
        if l != ".":
            if l not in antenna_dict.keys():
                antenna_dict[l] = [(x,y)]
            else:
                antenna_dict[l].append((x,y))
                
### part 1
antinode_pos = []
for a in antenna_dict.keys():
    antinode_pos += find_all_antinodes(antenna_dict[a])
antinode_pos = set(antinode_pos)
roof_size = [len(roof), len(roof[0])]
antinode_pos = [pos  for pos in antinode_pos if is_valid_pos(pos, roof_size)]
res1 = len(antinode_pos)
print("Solution 1:", res1)
            

### part 2
antinode_pos_2 = []
for a in antenna_dict.keys():
    antinode_pos_2 += find_all_antinodes_2(antenna_dict[a], roof_size)
antinode_pos_2 = set(antinode_pos_2)
res2 = len(antinode_pos_2)
print("Solution 2:", res2)
            