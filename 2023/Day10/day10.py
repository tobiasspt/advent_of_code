#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import numpy as np


"""
First index defines north and south. hihger x is further south
Second index defines east and west. higher y is further east
"""

def can_connect(pos1: tuple[int,int], pos2: tuple[int,int]) -> bool:
    xs, ys = pos1
    xn, yn = pos2
    testp = map_array[xn,yn]
    if xn - xs == 1:
        if testp in ["|", "L", "J"]:
            return True
    elif xn - xs == -1 :
        if testp in  ["|", "7", "F"]:
            return True
    elif yn - ys == 1:
        if testp in ["-", "7", "J"]:
            return True
    elif yn -ys == -1:
        if testp in ["-", "F", "L"]:
            return True
    return False


with open("input.txt", "r") as f:    
    A = f.read()


lines = A.split("\n")
line_list = [list(line) for line in lines]
map_array = np.array(line_list)

start_index = np.where(map_array == "S")
x = start_index[0][0]
y = start_index[1][0]
start_position = (x,y)



pipe_connection_set = set()
pipe_connection_set.add(start_position)

# Finding the first possible connection to the starting position
for nextp in [(x,y+1), (x-1, y), (y-1, x), (x+1, y)]:
    if can_connect(start_position, nextp):
        pipe_connection_set.add(nextp)
        currentp = nextp
        break

blocked_connections = set() # needed for part 2
while True:
    xc, yc = currentp
    current_pipe_type = map_array[xc, yc] 

    if current_pipe_type == "-":
        possible_next = [(xc, yc-1), (xc, yc+1)]
    elif current_pipe_type == "|":
        possible_next = [(xc-1, yc), (xc+1, yc)]
    elif current_pipe_type == "L":
        possible_next = [(xc-1, yc), (xc, yc+1)]
    elif current_pipe_type == "J":
        possible_next = [(xc-1, yc), (xc, yc-1)]
    elif current_pipe_type == "7":
        possible_next = [(xc+1, yc), (xc, yc-1)]
    elif current_pipe_type == "F":
        possible_next = [(xc+1, yc), (xc, yc+1)]
        
    for pn in possible_next:
        if pn == start_position:
            nextp = pn
        elif pn not in pipe_connection_set:
            pipe_connection_set.add(pn)
            nextp = pn
            break

    # Which connections are blocked by the connected pipes
    delta_x = currentp[0] - nextp[0]
    delta_y = currentp[1] - nextp[1]
    blocked_con = ((np.round(nextp[0]+delta_x/2,1), np.round(nextp[1]+delta_y/2,1)))
    blocked_connections.add(blocked_con)

    if nextp ==  start_position:
        break
    currentp = nextp

print(f"Solution 1:\n{int(len(pipe_connection_set)/2)}")


# Closing the circle, by adding the last bit of the blocked connections to the outside
x, y = start_position 
if can_connect(start_position, (x,y+1)):
    blocked_connections.add((x, y+0.5))
if can_connect(start_position, (x,y-1)):
    blocked_connections.add((x, y-0.5))
if can_connect(start_position, (x+1,y)):
    blocked_connections.add((x+0.5, y))
if can_connect(start_position, (x-1,y)):
    blocked_connections.add((x-0.5, y))



#%% Part 2

# Making a larger map and adding space between the tiles so that it is possible
# to squeeze through

map2 = np.zeros([map_array.shape[0]*2, map_array.shape[1]*2], dtype="<U1")
map2[:] = "x"

pipe_connection_set2 = set()

for x in range(map_array.shape[0]):
    for y in range(map_array.shape[1]):
        map2[x*2,y*2] = map_array[x,y]
        if (x,y) in pipe_connection_set:
            pipe_connection_set2.add((x*2,y*2))
            
for connection in blocked_connections:
    x,y = connection
    pipe_connection_set2.add((int(round(x*2)), int(round(y*2))))
    map2[int(round(x*2)), int(round(y*2))] = "+"


        
def get_neighbours(pos: tuple[int, int]) -> list[tuple[int,int]]:
    x, y = pos
    neighs = set([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
    neighs = [neigh for neigh in neighs if neigh[0] >= 0 and neigh[0] <= map2.shape[0]-1]
    neighs = [neigh for neigh in neighs if neigh[1] >= 0 and neigh[1] <= map2.shape[1]-1]
    return neighs
    

def leads_outside(pos: tuple[int, int]) -> bool:
    x, y = pos
    if x <= 0 or x >= map2.shape[0]-1:
        return True
    if y <= 0 or y >= map2.shape[1]-1:
        return True
    return False


lead_outside_set = set()
enclosed_tile_set = set()    


for x in range(map2.shape[0]):
    for y in range(map2.shape[1]):

        tile_to_check = (x,y)
        
        if tile_to_check in pipe_connection_set2:
            continue
        elif tile_to_check in lead_outside_set:
            continue
        elif tile_to_check in enclosed_tile_set:
            continue
        if leads_outside(tile_to_check):
            lead_outside_set.add(tile_to_check)
            continue
        
        tiles_to_check_set = set([tile_to_check]) #all tiles connected
        checked_tiles = set()

        while len(tiles_to_check_set) > 0:

            current_tile = tiles_to_check_set.pop()
            checked_tiles.add(current_tile)

            neighs = get_neighbours(current_tile)
            neighs = set([x for x in neighs if x not in pipe_connection_set2]) # filter out all pipes
            neighs = set([x for x in neighs if x not in checked_tiles and x not in tiles_to_check_set])

            leads_outside_bool = sum([1 for x in neighs if leads_outside(x) or x in lead_outside_set])
            
            if leads_outside_bool:
                lead_outside_set = lead_outside_set.union(set(tiles_to_check_set))
                lead_outside_set = lead_outside_set.union(checked_tiles)
                lead_outside_set = lead_outside_set.union(set(neighs))
                checked_tiles = set([])
                tiles_to_check_set = set([])
                
            else:
                tiles_to_check_set  = tiles_to_check_set.union(neighs)
        enclosed_tile_set = enclosed_tile_set.union(checked_tiles)
            
true_enclosed_tiles = [x for x in enclosed_tile_set if map2[x[0],x[1]] != "x"]
res2 = len(true_enclosed_tiles)
print(f"Solution 2:\n{res2}")



