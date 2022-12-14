# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np
import matplotlib.pyplot as plt

with open('input.txt', 'r') as f:
    A_input = f.read().split('\n')


#Parsing input
rocks_set = set()
for path in A_input:
    endpoints = path.split('->')
    for i in range(len(endpoints)-1):
        x_start,y_start = np.array(endpoints[i].split(','), dtype=int)
        x_end, y_end = np.array(endpoints[i+1].split(','), dtype=int)
        if x_start != x_end:
            for x_add in range(min([x_start, x_end]), max([x_start, x_end])+1):
                new_rock = (x_add, y_start)
                if new_rock not in rocks_set:
                    rocks_set.add(new_rock)     
        if y_start != y_end:
            for y_add in range(min([y_start, y_end]), max([y_start, y_end])+1):
                new_rock = (x_start, y_add)
                if new_rock not in rocks_set:
                    rocks_set.add(new_rock)
            
y_abiss = np.max([x[1] for x in rocks_set])
    

def plot_state(rocks, sands):
    
    fig = plt.figure()
    ax = fig.gca()
    
    rocks_x = [x[0] for x in rocks]
    rocks_y = [x[1] for x in rocks]
    sands_x = [x[0] for x in sands]
    sands_y = [x[1] for x in sands]
    
    ax.plot(rocks_x, rocks_y, 's', markersize=3)
    ax.plot(sands_x, sands_y, 'o', markersize=3)
    ax.invert_yaxis()
    


#%%

def move_sand(pos_sand, rocks, sands):
    
    y_new = pos_sand[1] + 1
    
    #I am freeeee, freeee faaling!
    if y_new == y_abiss+10:
        return [], None
    
    new_state = (pos_sand[0], y_new)
    if new_state not in rocks and new_state not in sands:
        return new_state, True
    
    x_new = pos_sand[0] - 1
    new_state = (x_new,y_new)
    if new_state not in rocks and new_state not in sands:
        return new_state, True
    
    x_new = pos_sand[0] + 1
    new_state = (x_new,y_new)
    if new_state not in rocks and new_state not in sands:
        return new_state, True
    
    # It came to a rest
    return pos_sand, False
    

def add_1_sand(rocks, sands):
    """
    Returns True if a sand came to rest
    Returns False if a sand falls into teh abiss
    """
    
    pos_sand = (500, 0) #starting position
     
    while True:
        pos_sand, res = move_sand(pos_sand, rocks, sands)
        
        if res is None:
            return [], False
        
        elif not res:
            return pos_sand, True
    

#Part 1
sands_set = set()
number_sands = 0

while True:
    pos_sand, res =  add_1_sand(rocks_set, sands_set)
    
    if not res:
        break
    
    sands_set.add(pos_sand)
    number_sands+=1
    
print(number_sands)


    
#%% Part two
# adding the floor
for i in range(500-(y_abiss+2)-10,500+(y_abiss+2)+10):
    rocks_set.add((i,y_abiss+2))

sands_set = set()
number_sands = 0

while True:
    pos_sand, res =  add_1_sand(rocks_set, sands_set)
    
    sands_set.add(pos_sand)
    number_sands+=1
    
    if pos_sand == (500,0):
        break
    
print(number_sands)


# plot_state(rocks_set, sands_set)
    
