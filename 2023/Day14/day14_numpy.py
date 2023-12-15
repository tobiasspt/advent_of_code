#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
import numpy as np
import copy

with open("input.txt", "r") as f:    
    A = f.read()
maparray_input = np.array([list(line) for line in A.split("\n")]) 

def total_load(map_array):
    load = 0
    xlen = map_array.shape[0]
    for i in range(xlen):
        load += sum(map_array[i] == "O") * (xlen -i)
    return load

def tilt_north(map_array: np.array) -> np.array:
    has_changed = True
    while has_changed:
        has_changed = False
        for x in range(1, map_array.shape[0]):
            for y in range(map_array.shape[1]):
                if map_array[x,y] == "O" and map_array[x-1,y] == ".":
                    map_array[x,y] = "."
                    map_array[x-1,y] = "O"
                    has_changed = True
    return map_array

def tilt_west(map_array: np.array) -> np.array:
    map_array = np.rot90(map_array,3)    
    map_array = tilt_north(map_array)
    map_array = np.rot90(map_array)
    return map_array

def tilt_south(map_array: np.array) -> np.array:
    map_array = np.rot90(map_array,2)    
    map_array = tilt_north(map_array)
    map_array = np.rot90(map_array,2)
    return map_array

def tilt_east(map_array: np.array) -> np.array:
    map_array = np.rot90(map_array,1)    
    map_array = tilt_north(map_array)
    map_array = np.rot90(map_array,3)
    return map_array

def tilt_cycle(map_array: np.array) -> np.array:
    return tilt_east(tilt_south(tilt_west(tilt_north(map_array))))

def print_array(map_array):
    print()
    for x in range(map_array.shape[0]):
        print("".join(map_array[x,:]))
        
def map_hash(map_array):
    x, y = np.where(map_array=="O")
    h = ",".join([str(i) for i in x]) + "|" + ",".join([str(i) for i in y])
    return h

def calculate_load_from_hash(maphash):
    load = 0
    xposis = np.array([int(x) for x in maphash.split("|")[0].split(",")])
    xlen = maparray_input.shape[0]

    for i in range(xlen):
        load += sum(xposis == i) * (xlen -i)
    return load


# Part 1
maparray_input = np.array([list(line) for line in A.split("\n")]) 
print(f"Solution 1:\n{total_load(tilt_north(copy.copy(maparray_input)))}")
print(f"Solution 1:\n{calculate_load_from_hash(map_hash(tilt_north(copy.copy(maparray_input))))}")


#%%## Part 2
# I am looking for the reoccurance fo the same pattern again 
total_cycles = 1000000000
map_array = copy.deepcopy(maparray_input)

hash_table = dict()    
map_hash(map_array)

for i in range(total_cycles):
    current_hash = map_hash(map_array)
    if current_hash in hash_table:
        old_time = hash_table[current_hash][-1]
        new_time = i
        break
    else:
        hash_table[current_hash] = [i]
    map_array = tilt_cycle(map_array)
    
time_we_need = (total_cycles-old_time)%(new_time-old_time) + old_time
#find the right hash
for h in hash_table.keys():
    if hash_table[h][0] == time_we_need:
        hash_at_total_cycles = h
        break
    
res2 = calculate_load_from_hash(hash_at_total_cycles)
print(f"Solution 2\n{res2}")


