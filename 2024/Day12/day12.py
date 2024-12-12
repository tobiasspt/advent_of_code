#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
def get_neighs(pos: tuple[int,int], size:list[int,int], outside: bool=False) -> list[tuple[int,int]]:
    x,y = pos
    mx,my = size
    neighs = []
    
    if not outside:
        if x > 0:
            neighs.append((x-1,y))
        if x < mx-1:
            neighs.append((x+1,y))
        if y > 0:
            neighs.append((x,y-1))
        if y < my-1:
            neighs.append((x,y+1))   
         
    if outside: 
        neighs.append((x-1,y))
        neighs.append((x+1,y))
        neighs.append((x,y-1))
        neighs.append((x,y+1))   
    return neighs

def find_all_connected_plots(pos: tuple[int,int], fruit: str, garden: list[list[str]]) -> list[tuple[int,int]]:
    
    garden_size = (len(garden[0]), len(garden))
    pos_to_check = [pos]
    pos_checked = []
    
    while len(pos_to_check) > 0:
        cp = pos_to_check.pop()
        pos_checked.append(cp)
        neighs = get_neighs(cp, garden_size)
        neighs = [p for p in neighs if p not in pos_checked] ## already captured
        neighs = [p for p in neighs if garden[p[1]][p[0]]==fruit] ## different region
        for n in neighs:
            pos_to_check.append(n)
    return list(set(pos_checked))


def area(region: list[tuple[int,int]]) -> int:
    return len(region)

def perimeter(region: list[tuple[int,int]], size: list[int,int]) -> int:
    perim = 0
    for plot in region:
        neighs = get_neighs(plot, size, outside=True)
        perim += sum([1 for n in neighs if n not in region]) 
    return perim 
    
def prize(region: list[tuple[int,int]], size: list[int,int]) -> int:
    return area(region) * perimeter(region, size)

def count_sides_from_fences(fences: list(tuple[int,int]), xory: int) -> int:
    n_sides = 0
    fence_lines = set([x[xory] for x in fences])
    for fl in fence_lines:
        fl_spots = [f[(xory+1)%2] for f in fences if f[xory] == fl]
        fl_spots = sorted(fl_spots)
        n_sides += 1
        if len(fl_spots) == 1:
            continue
        for ii in range(len(fl_spots[:-1])):
            if fl_spots[ii+1]-fl_spots[ii] > 1.1:
                n_sides += 1
    return n_sides

def number_sides(region: list[tuple[int,int]]) -> int:
    fence_0 = []
    fence_1 = []
    fence_2 = []
    fence_3 = []
    
    for plot in region:
        neighs = get_neighs(plot, [0,0], outside=True)
        neighs =[n for n in neighs if n not in region]
        x,y = plot
        for n in neighs:
            nx,ny = n
            dx = nx - x
            dy = ny - y
            if dx == 1:
                fence_1.append((x,y))
            elif dx == -1:
                fence_3.append((x,y))
            elif dy == 1:
                fence_2.append((x,y))
            elif dy == -1:
                fence_0.append((x,y))
        
    n_sides = count_sides_from_fences(fence_0, 1) 
    n_sides += count_sides_from_fences(fence_1, 0)
    n_sides += count_sides_from_fences(fence_2, 1)
    n_sides += count_sides_from_fences(fence_3, 0)
    return n_sides

def prize_2(region: list[tuple[int,int]]) -> int:
    return area(region) * number_sides(region)


#%%


with open("input.txt", "r") as f:    
    A = f.read()
## reading input and defining regions
garden = list([list(line) for line in A.split()])
garden_plot_done = []
region_dict = {}
region_counter = 0
for y, line in enumerate(garden):
    for x, fruit in enumerate(line):
        if (x,y) in garden_plot_done:
            continue
        else:
            garden_plot_done.append((x,y))    
        current_id = region_counter
        region_counter += 1
        region = find_all_connected_plots((x,y), fruit, garden)
        region_dict[region_counter] = region
        garden_plot_done += region
        

## part 1
garden_size = [len(region[0]), len(region)]
res1 = sum([prize(region_dict[key], garden_size) for key in region_dict.keys()])
print("Solution 1:", res1)

## part 2
res2 = sum([prize_2(region_dict[key]) for key in region_dict.keys()])
print("Solution 2:", res2)

