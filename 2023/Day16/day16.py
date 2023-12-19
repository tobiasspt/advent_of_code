#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
### Solution works, but is rather slow")

with open("input.txt", "r") as f:    
    A = f.read()


mirror_array = [list(line) for line in A.split("\n")]
xlen = len(mirror_array)
ylen = len(mirror_array[0])


def print_tiles(energized_tiles_set):
    for x in range(xlen):
        s = ""
        for y in range(ylen):
            if (x,y) in energized_tiles_set:
                s+= "#"
            else:
                s+='.'
        print(s)


def get_next_positions(path):
    x, y, direc = path
    new_paths = []
    energized_tiles = set()
    if direc == "r":
        newy = y+1
        if newy >= ylen:
            return [], set()
        next_tile =  mirror_array[x][newy]
        energized_tiles.add((x, newy))
        
        if next_tile in ["-","."]:
            new_paths.append([x, newy, "r"])
        elif next_tile == "/":
            new_paths.append([x, newy, "u"])
        elif next_tile == "\\":
            new_paths.append([x, newy, "d"])
        elif next_tile == "|":
            new_paths += [[x, newy, "u"],[x, newy, "d"]]


    elif direc == "l":
        newy = y-1
        if newy < 0 :
            return [], set()
        next_tile =  mirror_array[x][newy]
        energized_tiles.add((x, newy))
        
        if next_tile in ["-","."]:
            new_paths.append([x, newy, "l"])
        elif next_tile == "/":
            new_paths.append([x, newy, "d"])
        elif next_tile == "\\":
            new_paths.append([x, newy, "u"])
        elif next_tile == "|":
            new_paths += [[x, newy, "u"],[x, newy, "d"]]


    elif direc == "d":
        newx = x+1
        if newx >= xlen:
            return [], set()
        next_tile =  mirror_array[newx][y]
        energized_tiles.add((newx, y))
        
        if next_tile in ["|","."]:
            new_paths.append([newx, y, "d"])
        elif next_tile == "/":
            new_paths.append([newx, y, "l"])
        elif next_tile == "\\":
            new_paths.append([newx, y, "r"])
        elif next_tile == "-":
            new_paths += [[newx, y, "l"],[newx, y, "r"]]

    
    elif direc == "u":
        newx = x-1
        if newx < 0:
            return [], set()
        next_tile =  mirror_array[newx][y]
        energized_tiles.add((newx, y))
        
        if next_tile in ["|","."]:
            new_paths.append([newx, y, "u"])
        elif next_tile == "/":
            new_paths.append([newx, y, "r"])
        elif next_tile == "\\":
            new_paths.append([newx, y, "l"])
        elif next_tile == "-":
            new_paths += [[newx, y, "l"],[newx, y, "r"]]

    
    new_paths = [path for path in new_paths if path[0] >=0 and path[0] < xlen]
    new_paths = [path for path in new_paths if path[1] >=0 and path[1] < ylen]
    energized_tiles = energized_tiles.union(set([(x[0],x[1]) for x in new_paths]))

    return new_paths, energized_tiles


def path_hash(path):
    return str(path[0])+','+str(path[1])+","+path[2]

def get_number_of_energized_tiles(initial_path):
    paths_to_check = [initial_path]
    
    tile_set = set()
    energized_tiles_set = set()
    
    while len(paths_to_check) > 0:
        path = paths_to_check[0]
        paths_to_check.remove(path)
        if path_hash(path) in tile_set:
            continue
        else:
            tile_set.add(path_hash(path))
        new_paths, energized_tiles = get_next_positions(path)

        energized_tiles_set = energized_tiles_set.union(energized_tiles)
        paths_to_check += new_paths
        
        
    return len(energized_tiles_set)
res1 = get_number_of_energized_tiles([0,-1,"r"])

    
print(f"Solution 1\n{res1}")
        

###  Part 2
number_of_energized_tiles = []

for x in range(xlen):
    n1 = get_number_of_energized_tiles([x, -1, "r"])
    n2 = get_number_of_energized_tiles([x, ylen, "l"])
    number_of_energized_tiles += [n1,n2]
    
for y in range(ylen):
    n1 = get_number_of_energized_tiles([-1, y, "d"])
    n2 = get_number_of_energized_tiles([xlen, y, "u"])
    number_of_energized_tiles += [n1,n2]
    
print(f"Solution 2\n{max(number_of_energized_tiles)}")
    
    
    
    