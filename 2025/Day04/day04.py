#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import numpy as np


def get_subgrid(x: int, y: int, grid: np.ndarray) -> np.ndarray:
    xmin = x-1
    xmax = x+2
    ymin = y-1
    ymax = y+2
    size = grid.shape[0]

    if x == 0: xmin = 0
    if y == 0: ymin = 0
    if x == size-1: xmax = size
    if y == size-1: ymax = size
    
    return grid[xmin:xmax, ymin:ymax]
    

def get_removable_paper_rolls(grid: np.ndarray) -> list[tuple[int,int]]:
    accessible_paper_rolls = []
    for x in range(grid.shape[0]):
        for y in range(grid.shape[0]):
            if grid[x,y] == "@":
                subgrid = get_subgrid(x, y, grid)
                if sum(sum(subgrid=="@")) < 5: ## the middel one counts as well
                    accessible_paper_rolls.append((x,y))
    return accessible_paper_rolls
            

## Input reading
with open("input.txt", "r") as f:    
    A = f.read()
grid = np.array([list(x) for x in A.split("\n")], dtype=str)

## Part 1
print(f"Soluton 1: {len(get_removable_paper_rolls(grid))}")
        
## Part 2
new_grid = grid
removed_paper_rolls = 0
while True:
    removable_rolls = get_removable_paper_rolls(new_grid)
    removed_paper_rolls += len(removable_rolls)
    for x,y in removable_rolls:
        new_grid[x,y] = "."
    if len(removable_rolls) == 0:
        break
print(f"Solution 2: {removed_paper_rolls}")
        
        