#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: tobias
"""

from collections import defaultdict


def rectangle_area(tile1: tuple[int,int], tile2: tuple[int,int]) -> int:
    x1, y1 = tile1
    x2, y2 = tile2
    area = (abs(x1-x2) + 1) * (abs(y1-y2) + 1)
    return area

def get_edge_ranges(red_tiles: list[list[int,int]]) -> tuple[list[list[int,int]], list[list[int,int]]]:
    
    x_ranges = defaultdict(lambda: [])  ## horizontal
    y_ranges = defaultdict(lambda: [])  ## vertical

    for i, tile1 in enumerate(red_tiles[:-1]):
        tile2  = red_tiles[i+1]
            
        x1,y1 = tile1 
        x2,y2 = tile2
        
        if x1 == x2:
            y_ranges[x1].append((min(y1,y2), max(y1,y2)))
        if y1 == y2:
            x_ranges[y1].append((min(x1,x2), max(x1,x2)))
            
    ## add the last tile to the first
    tile2 = red_tiles[-1]
    tile1 = red_tiles[0]

    x1,y1 = tile1 
    x2,y2 = tile2
    if x1 == x2:
        y_ranges[x1].append((min(y1,y2), max(y1,y2)))
    if y1 == y2:
        x_ranges[y1].append((min(x1,x2), max(x1,x2)))
    return x_ranges, y_ranges


def range1_in_range2(range1: tuple[int,int], range2: tuple[int,int]) -> bool:
    s1, e1 = range1
    s2, e2 = range2
    if s1 > e2:
        return False
    if e1 < s2:
        return False
    return True


def rectangle_in_green(tile1: tuple[int,int], tile2: tuple[int,int], x_ranges: tuple[int,int], y_ranges: tuple[int,int]) -> bool:
    ## If an edge intersects the rectangle, it is not only within green and red tiles
    x1, y1 = tile1 
    x2, y2 = tile2
    
    minx = min(x1,x2)
    maxx = max(x1,x2)
    
    miny = min(y1,y2)
    maxy = max(y1,y2)
    
    ## Check for a vertical intersection
    x_keys = y_ranges.keys()
    
    for xkey in x_keys:
        if minx < xkey < maxx:
            for r1 in y_ranges[xkey]:
                if range1_in_range2(r1, (miny+1, maxy-1)):
                    return False
            
    ## Check for a horizontal intersection
    y_keys = x_ranges.keys()
    for ykey in y_keys:
        if miny < ykey < maxy:
            for r1 in x_ranges[ykey]:
                if range1_in_range2(r1, (minx+1, maxx-1)):
                    return False
    
    return True


### Reading and parsing input
with open("input.txt", "r") as f:    
    A = f.read()
red_tiles = [[int(x) for x in y.split(",")] for y in A.split("\n")]



### Part 1
max_area = 0
for i, tile1 in enumerate(red_tiles[:-1]):
    for tile2 in red_tiles[i+1:]:
        area = rectangle_area(tile1, tile2)
        if area > max_area:
            max_area = area
print(f"Solution 1: {max_area}")
        

### Part 2
x_ranges, y_ranges = get_edge_ranges(red_tiles)
max_area2 = 0
for i, tile1 in enumerate(red_tiles[:-1]):
    for tile2 in red_tiles[i+1:]:
        area = rectangle_area(tile1, tile2)
        if area <= max_area2:
            continue
        else:
            if  rectangle_in_green(tile1, tile2, x_ranges, y_ranges):
                max_area2 = area
print(f"Solution 2: {max_area2}")
        
        









