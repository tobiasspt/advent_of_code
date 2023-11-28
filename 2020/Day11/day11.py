#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import matplotlib.pyplot as plt
import numpy as np
import copy
import itertools

with open("input.txt", "r") as f:    
    A = f.read()
    
    
# A = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL"""

lines = A.split('\n')
lines = [list(line) for line in lines]

seats = np.array(lines)

n_rows, n_cols = seats.shape

#%% Part 1
def get_neighbours(pos):
    neighbours = []
    for r, c in itertools.product(range(pos[0]-1, pos[0]+2), range(pos[1]-1, pos[1]+2)):
        if r < 0 or r >= n_rows:
            continue
        elif c < 0 or c >= n_cols:
            continue
        elif r==pos[0] and c == pos[1]:
            continue
        neighbours.append((r,c))
    return neighbours
        

# Prepare seat dictionary
seat_dict = {}
for r, c in itertools.product(range(n_rows), range(n_cols)):
    pos = (r, c)
    if seats[r,c] == ".":
        seat_dict[pos] = {"status":'.', "neighbours":[]}
        continue
    else:
        neighbours = get_neighbours(pos)
        neighbours = [x for x in neighbours if seats[x[0],x[1]] != "."] #leaf out floor seats
        seat_dict[pos] = {"status":"L", "neighbours":neighbours}
        
        
def empty_seat(pos: tuple, seats: list[list[str]]) ->bool:
    neighbours = seat_dict[pos]["neighbours"]
    full_seats = 0
    for neigh in neighbours:
        if seats[neigh[0]][neigh[1]] =="#": full_seats+=1 
        
    if full_seats >= 4:
        return True
    else: 
        return False
    
def fill_seat(pos: tuple, seats: list[list[str]]) ->bool:
    neighbours = seat_dict[pos]["neighbours"]
    for neigh in neighbours:
        if seats[neigh[0]][neigh[1]]=="#":
            return False        
    return True
        


seats_current = copy.deepcopy(seats)
seats_new = copy.deepcopy(seats)

n_steps = 0
changed_in_this_step = True

while changed_in_this_step:
    
    n_steps += 1
    changed_in_this_step = False
    
    for r, c in itertools.product(range(n_rows), range(n_cols)):
        pos = (r, c)
        
        if seat_dict[pos] == ".":
            continue
        
        elif seats_current[r][c] == "L":
            fill = fill_seat(pos, seats_current)
            if fill:
                changed_in_this_step = True
                seats_new[r][c] = "#"


        elif seats_current[r][c] == "#":
            empty = empty_seat(pos, seats_current)
            if empty:
                # print('hi')
                changed_in_this_step = True
                seats_new[r][c] = "L"
                
    seats_current = copy.deepcopy(seats_new)
    
solution1 = sum([sum(np.array(x)=="#") for x in seats_current]) 
print(f"Solution 1:\n{solution1}")

#%% Part 2
def get_neighbours2(pos):
    neighbours = []
    
    # eight directions
    
    #dir 1: nr +1
    nr = pos[0]
    nc = pos[1]
    while True:
        nr += 1
        if nr >= n_rows:
            break
        if seats[nr][nc] == "L":
            neighbours.append((nr, nc))
            break
    #dir 2 nr +1, nc + 1
    nr = pos[0]
    nc = pos[1]
    while True:
        nr += 1
        nc += 1
        if nr >= n_rows:
            break
        if nc >= n_cols:
            break
        if seats[nr][nc] == "L":
            neighbours.append((nr, nc))
            break
    # direction 3 nc += 1
    nr = pos[0]
    nc = pos[1]
    while True:
        nc += 1
        if nc >= n_cols:
            break
        if seats[nr][nc] == "L":
            neighbours.append((nr, nc))
            break
    # direction 4 nc += 1, nr = -1   #!!! fishy!!!
    nr = pos[0]
    nc = pos[1]
    while True:
        nc += 1
        nr += -1
        if nc >= n_cols:
            break
        if nr < 0:
            break
        if seats[nr][nc] == "L":
            neighbours.append((nr, nc))
            break
    # direction 5, nr = -1
    nr = pos[0]
    nc = pos[1]
    while True:
        nr += -1
        if nr < 0:
            break
        if seats[nr][nc] == "L":
            neighbours.append((nr, nc))
            break
    # direction 6, nr = -1, nc = -1 
    nr = pos[0]
    nc = pos[1]
    while True:
        nr += -1
        nc += -1 
        if nr < 0:
            break
        if nc < 0:
            break
        if seats[nr][nc] == "L":
            neighbours.append((nr, nc))
            break
    # direction 7, nc = -1 
    nr = pos[0]
    nc = pos[1]
    while True:
        nc += -1 
        if nc < 0:
            break
        if seats[nr][nc] == "L":
            neighbours.append((nr, nc))
            break
    # direction 8, nc = -1 , nr = 1
    nr = pos[0]
    nc = pos[1]
    while True:
        nc += -1 
        nr += 1
        if nc < 0:
            break
        if nr >= n_rows:
            break
        if seats[nr][nc] == "L":
            neighbours.append((nr, nc))
            break
    

    return neighbours
        

# Prepare seat dictionary
seat_dict2 = {}
for r, c in itertools.product(range(n_rows), range(n_cols)):
    pos = (r, c)
    if seats[r,c] == ".":
        seat_dict2[pos] = {"status":'.', "neighbours":[]}
        continue
    else:
        neighbours = get_neighbours2(pos)
        neighbours = [x for x in neighbours if seats[x[0],x[1]] != "."] #leaf out floor seats
        seat_dict2[pos] = {"status":"L", "neighbours":neighbours}
        
        
def empty_seat(pos: tuple, seats: list[list[str]]) ->bool:
    neighbours = seat_dict2[pos]["neighbours"]
    full_seats = 0
    for neigh in neighbours:
        if seats[neigh[0]][neigh[1]] =="#": full_seats+=1 
        
    if full_seats >= 5:
        return True
    else: 
        return False
    
def fill_seat(pos: tuple, seats: list[list[str]]) ->bool:
    neighbours = seat_dict2[pos]["neighbours"]
    for neigh in neighbours:
        if seats[neigh[0]][neigh[1]]=="#":
            return False        
    return True
        


seats_current = copy.deepcopy(seats)
seats_new = copy.deepcopy(seats)

n_steps = 0
changed_in_this_step = True

while changed_in_this_step:
    
    n_steps += 1
    changed_in_this_step = False
    
    for r, c in itertools.product(range(n_rows), range(n_cols)):
        pos = (r, c)
        
        if seat_dict2[pos] == ".":
            continue
        
        elif seats_current[r][c] == "L":
            fill = fill_seat(pos, seats_current)
            if fill:
                changed_in_this_step = True
                seats_new[r][c] = "#"


        elif seats_current[r][c] == "#":
            empty = empty_seat(pos, seats_current)
            if empty:
                # print('hi')
                changed_in_this_step = True
                seats_new[r][c] = "L"
                
    seats_current = copy.deepcopy(seats_new)
    
solution2 = sum([sum(np.array(x)=="#") for x in seats_current]) 
print(f"Solution 2:\n{solution2}")



        