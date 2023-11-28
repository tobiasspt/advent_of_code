#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
from collections import Counter
import numpy as np


with open("input.txt", "r") as f:    
    A = f.read()
tiles = A.split('\n\n')

def get_borders(image):
    b1 = tuple(image[0,:])
    b2 = tuple(image[:,-1])
    b3 = tuple(image[-1,:][:])
    b4 = tuple(image[:,0][:])
    return b1,b2,b3,b4



tile_dict = {}
border_list = []


for tile in tiles:
    
    lines = tile.split('\n')
    name = lines[0].split()[1][:-1]
    lines_list = [list(line) for line in lines[1:]]
    image = np.array(lines_list)
    borders = list(get_borders(image))

    border_list += list(get_borders(image))
    tile_dict[name] = {"image": image, "borders": borders}



#%% Part 1

# The reconstruction of the image is not necessary for part 1, as the
# knowledge of the four tiles with TWO unique boarders is sufficient. 

border_counter = Counter(border_list) #how many instances of a border are there

solution1 = 1
for tile in tile_dict:
    uniqe_borders = 0
    for border in tile_dict[tile]["borders"]:
        if border_counter[border] == 1 and border_counter[border[::-1]] == 0:
            uniqe_borders += 1
    if uniqe_borders == 2:
        solution1 *= float(tile)
print(f"Solution 1:\n{int(solution1)}")


#%% Part 2
"""
Part two actually needs the image reconstructed. 
After some inspection of the tiles (with code not shown in this script):
     - there are 4 tiles with TWO unique borders -> corners
     - 40 (=12*4-8) tiles with ONE unique border -> edges
     - No border appears more than TWICE
         -> finding one matchin border is sufficent!
"""

"""
My borders are enumerated as
  0  
3   1  
  2 

grid:
 0 12 ... 132
 1 
 2
 .
 .
11    ... 143
"""


def rot0(tile):
    return tile
def rot1(tile):
    return np.rot90(tile)
def rot2(tile):
    return np.rot90(rot1(tile))
def rot3(tile):
    return np.rot90(rot2(tile))

def flip0(tile):
    return tile[:,::-1]
def flip1(tile):
    return rot1(tile)[:,::-1]
def flip2(tile):
    return rot2(tile)[:,::-1]
def flip3(tile):
    return rot3(tile)[:,::-1]  



N_tiles = len(tile_dict)
grid_len = int(np.sqrt(N_tiles))


# image reconstruction
grid = {}
for i in range(N_tiles):
    grid[i] = {}
    
    
tiles_left_to_place = list(tile_dict.keys())

# finding the first corner
for tile in tile_dict:
    uniqe_borders = 0
    which = []
    for i, border in enumerate(tile_dict[tile]["borders"]): 
        if border_counter[border] == 1 and border_counter[border[::-1]] == 0:
            uniqe_borders += 1
            which.append(i)
    if uniqe_borders == 2:
        grid[0]["tile"] = tile
        if which ==[2,3]:
            new_tile = rot3(tile_dict[tile]["image"])
        elif which == [1,2]:
            new_tile = rot2(tile_dict[tile]["image"])
        elif which == [0,1]:
            new_tile = rot1(tile_dict[tile]["image"])
        elif which == [0,3]:
            new_tile = tile_dict[tile]["image"]
        else:
            print("something went wrong")
            3/0    
        borders = get_borders(new_tile)
        grid[0]["image"] = new_tile
        grid[0]["borders"] = borders
        tiles_left_to_place.remove(tile)
        break


#Completeing the first line
for i in range(1, grid_len):
    
    border_to_match = grid[i-1]["borders"][1]
    found_bool = False
    for tile in tiles_left_to_place:
        if found_bool:
            break
        for fun in [rot0, rot1, rot2, rot3, flip0, flip1, flip2, flip3]:
            new_tile = fun(tile_dict[tile]["image"])
            new_borders = get_borders(new_tile)
            if border_to_match == new_borders[3]:
                grid[i] = {"tile":tile, "image":new_tile, "borders":new_borders}
                found_bool = True
                tiles_left_to_place.remove(tile)
                break
                

# Completing the the rest
for y in range(1,grid_len):
    for i in range(grid_len):
        # Next tile to match
        grid_spot = y*grid_len + i
   
        border_to_match = grid[grid_spot-grid_len]["borders"][2]
        found_bool = False
        for tile in tiles_left_to_place:
            if found_bool:
                break
            for fun in [rot0, rot1, rot2, rot3, flip0, flip1, flip2, flip3]:
                new_tile = fun(tile_dict[tile]["image"])
                new_borders = get_borders(new_tile)
                if border_to_match == new_borders[0]:
                    grid[grid_spot] = {"tile":tile, "image":new_tile, "borders":new_borders}
                    found_bool = True
                    tiles_left_to_place.remove(tile)
                    break
        

# Image merging to the large image
tile_size = grid[0]["image"].shape[0]
place_size = tile_size-2
image_size = (tile_size-2)*grid_len
large_image = np.zeros([image_size, image_size], dtype='<U1')

for grid_spot in grid:
    x = grid_spot//grid_len
    y = grid_spot%grid_len
    image_to_place = grid[grid_spot]["image"][1:-1,1:-1]
    large_image[x*place_size:(x+1)*place_size, y*place_size:(y+1)*place_size] = image_to_place


#%% monster hunt
"""
--------------------
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
 -------------------
"""


monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

monster_coords = []
for y, line in enumerate(monster.split('\n')):
    for x, char in enumerate(line):
        if char == "#":
            monster_coords.append((x,y))
            
monster_amount = 0
for function in [rot0, rot1, rot2, rot3, flip0, flip1, flip2, flip3]:
    large_image_new = function(large_image)    
    for xstart in range(image_size-19):
        for ystart in range(image_size-2):
            res = sum([1 for x,y in monster_coords if large_image_new[y + ystart, x + xstart]=="#"])

            if res == len(monster_coords):             
                monster_amount += len(monster_coords)

solution2 = np.sum(large_image == "#" ) - monster_amount
print(f"Solution 2:\n{solution2}")



