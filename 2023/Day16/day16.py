#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
from collections import deque

"""
directions:
0 = up
1 = right
2 = down
3 = left
"""
def get_next_ways(nx: int, ny: int, direc: int, mirror: str) -> list[tuple[int,int,int]]:
    if direc == 0: ## up
        if mirror == "|":
            next_ways = [(nx,ny,0)]
        elif mirror == "-":
            next_ways = [(nx,ny,1), (nx,ny,3)]
        elif mirror == "/":
            next_ways = [(nx,ny,1)]
        elif mirror == "\\":
            next_ways = [(nx,ny,3)]
            
    elif direc == 2: ## down
        if mirror == "|":
            next_ways = [(nx,ny,2)]
        elif mirror == "-":
            next_ways = [(nx,ny,1), (nx,ny,3)]
        elif mirror == "/":
            next_ways = [(nx,ny,3)]
        elif mirror == "\\":
            next_ways = [(nx,ny,1)]
            
    elif direc == 1: ## right
        if mirror == "|":
            next_ways = [(nx,ny,0), (nx,ny,2)]
        elif mirror == "-":
            next_ways = [(nx,ny,1)]
        elif mirror == "/":
            next_ways = [(nx,ny,0)]
        elif mirror == "\\":
            next_ways = [(nx,ny,2)]

    elif direc == 3: ## left
        if mirror == "|":
            next_ways = [(nx,ny,0), (nx,ny,2)]
        elif mirror == "-":
            next_ways = [(nx,ny,3)]
        elif mirror == "/":
            next_ways = [(nx,ny,2)]
        elif mirror == "\\":
            next_ways = [(nx,ny,0)]   

    return next_ways




pos_to_pos_dict = {}
def position_to_position(sx: int, sy: int, sdirec: int, mirror_array: list[list[str]]) -> list[tuple[int,int]]:
    # From any place to a mirror or to the outside.
    # There might be more than one end-place (beam_split).
    # Function returns:
    # - the tiles which are energyzed (including the start tile)
    # - the outgoing directions
    
    x = sx
    y = sy
    direc = sdirec
    
    ## The results of the function are memorized
    if (x,y,direc) in pos_to_pos_dict.keys():
        return pos_to_pos_dict[(sx,sy,sdirec)]["next_ways"], pos_to_pos_dict[(x,y,direc)]["energized_tiles"]
    
    if x>=0 and x< len(mirror_array[0]) and y>=0 and y< len(mirror_array):
        pos_energyzed = [(x,y)]
    else:
        pos_energyzed = []
    
    while True: ## moving till mirror or outside
      
        #moving to next tile
        if direc == 0:
            ny = y - 1
            nx = x
        elif direc == 1:
            ny = y
            nx = x + 1     
        elif direc == 2:
            ny = y + 1
            nx = x              
        elif direc == 3:
            ny = y
            nx = x - 1     
    
        ## left the area
        if nx < 0 or nx >= len(mirror_array[0]):
            next_ways = []
            pos_to_pos_dict[(sx,sy,sdirec)] = {"next_ways": next_ways, "energized_tiles": pos_energyzed}
            return next_ways, pos_energyzed
        if ny < 0 or ny >= len(mirror_array):
            next_ways = []
            pos_to_pos_dict[(sx,sy,sdirec)] = {"next_ways": next_ways, "energized_tiles": pos_energyzed}
            return next_ways, pos_energyzed
        
        # the tile tried is a mirror! 
        if mirror_array[ny][nx] != ".":
            ## do the mirror magic
            mirror = mirror_array[ny][nx]
            next_ways =  get_next_ways(nx, ny, direc, mirror)
            pos_to_pos_dict[(x,y,direc)] = {"next_ways": next_ways, "energized_tiles": pos_energyzed}
            return next_ways, pos_energyzed
            
        ## continue walking
        x = nx
        y = ny
        pos_energyzed.append((nx,ny))
    
    

def get_energized_tiles(start: tuple[int,int,int], mirror_array: list[list[str]]) -> list[tuple[int,int]]:
    
    handeled_positions = []
    next_ways_stack = deque([start])
    energized_tiles = []
    
    while len(next_ways_stack) > 0:
        nn = next_ways_stack.pop()
        if nn in handeled_positions:
            continue
        else:
            handeled_positions.append(nn)
        
        x,y,direc = nn
        new_ways, new_et = position_to_position(x, y, direc, mirror_array)
        energized_tiles += new_et
        
        for nw in new_ways:
            if nw not in handeled_positions:
                next_ways_stack.append(nw)
    
    ## all done. exit from llop and return
    return set(energized_tiles)


### input reading
with open("input.txt", "r") as f:    
    A = f.read()
mirror_array = [list(line) for line in A.split("\n")]
ylen = len(mirror_array)
xlen = len(mirror_array[0])


### part 1
energyzed_tiles = get_energized_tiles((-1,0,1), mirror_array)
res1 = len(energyzed_tiles)
print("Solution 1:", res1)


###  part 2
number_of_energized_tiles = []
for y in range(ylen):
    n1 = len(get_energized_tiles([-1, y, 1], mirror_array))
    n2 = len(get_energized_tiles([xlen, y, 3], mirror_array))
    number_of_energized_tiles += [n1,n2]
for x in range(xlen):
    n1 = len(get_energized_tiles([x, -1, 2], mirror_array))
    n2 = len(get_energized_tiles([x, ylen, 0], mirror_array))
    number_of_energized_tiles += [n1,n2]
print(f"Solution 2: {max(number_of_energized_tiles)}")

    
    