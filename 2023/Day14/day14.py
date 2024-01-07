#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

with open("input.txt", "r") as f:    
    A = f.read()


map_lines = A.split("\n")
row_len = len(map_lines[0])
col_len = len(map_lines)

def rotate_map(map_lines: list[str]) -> list[str]:
    return  ["".join(x[i] for x in map_lines) for i in range(len(map_lines))]


def tilt_north(map_lines: list[str]) -> list[str]:
    return ["#".join(["".join(sorted(x, reverse=True)) for x in line.split("#")]) for line in map_lines]


def tilt_south(map_lines: list[str]) -> list[str]:
    
    map_lines = [x[::-1] for x in map_lines]
    map_lines = tilt_north(map_lines)
    map_lines = [x[::-1] for x in map_lines]
    return map_lines

def tilt_west(map_lines: list[str]) -> list[str]:
    
    map_lines = rotate_map(map_lines)
    map_lines = tilt_north(map_lines)
    map_lines = rotate_map(map_lines)
    return map_lines

def tilt_east(map_lines: list[str]) -> list[str]:
    
    map_lines = rotate_map(map_lines)
    map_lines = tilt_south(map_lines)
    map_lines = rotate_map(map_lines)
    return map_lines


def total_load(map_lines: list[str])-> int:
    load = 0
    xlen = len(map_lines)
    for i in range(xlen):
        load += map_lines[i].count("O") * (xlen -i)
    return load


def map_hash(map_lines: list[str]) -> str:
    h = "".join(map_lines)
    return h


def calculate_load_from_hash(maphash: str) -> list[str]:
    map_lines = [maphash[idx : idx + col_len] for idx in range(0, len(maphash), col_len)]
    map_lines = rotate_map(map_lines)
    return total_load(map_lines)


def print_map(map_lines: list[str]) -> None:
    foo =  ["".join(x[i] for x in map_lines) for i in range(len(map_lines))]
    print()
    for line in foo:
        print(line)


def tilt_cycle(map_lines: list[str]) -> list[str]:
    return tilt_east(tilt_south(tilt_west(tilt_north(map_lines))))


# Part 1
map_lines = A.split("\n")
map_lines = rotate_map(map_lines) #facing north
map_lines = tilt_north(map_lines)
print(f"Solution 1:\n{total_load(rotate_map(tilt_north(map_lines)))}")
# print(f"Solution 1:\n{calculate_load_from_hash(map_hash(tilt_north(map_lines)))}")


#%%### Part 2
# I am looking for the reoccurance fo the same pattern again 

total_cycles = 1000000000

map_lines = A.split("\n")
map_lines = rotate_map(map_lines) #facing north
    
hash_table = dict()    

for i in range(total_cycles):    
    current_hash = map_hash(map_lines)
    if current_hash in hash_table:
        
        old_time = hash_table[current_hash][-1]
        new_time = i
        break
    else:
        hash_table[current_hash] = [i]
    map_lines = tilt_cycle(map_lines)

    
time_we_need = (total_cycles-old_time)%(new_time-old_time) + old_time
#find the right hash
for h in hash_table.keys():
    if hash_table[h][0] == time_we_need:
        hash_at_total_cycles = h
        break
    
res2 = calculate_load_from_hash(hash_at_total_cycles)
print(f"Solution 2\n{res2}")

