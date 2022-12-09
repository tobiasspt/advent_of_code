# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np

with open('input.txt', 'r') as f:
    A_input = f.read()
    
arr = []
for line in A_input.split('\n'):
    arr.append(list(line))
arr = np.array(arr, dtype=int)
size = arr.shape[0] #Program does not account for non-square shape

#%%
#Part1
# How many trees are visible from outside the grid?

vis = np.zeros_like(arr)


for x in range(size):
    
    visible = False

    for y in range(size):
        #edge cases are always visible
        if x == 0 or x == size-1  or y == 0 or y == size-1:
            vis[x,y]  = 1
            continue

        # up
        if np.all(arr[:x,y]< arr[x,y]):
            vis[x,y] = 1
            continue
        elif np.all(arr[x+1:,y] < arr[x,y]):
            vis[x,y] = 1
            continue
        elif np.all(arr[x,:y]< arr[x,y]):
            vis[x,y] = 1
            continue
        elif np.all(arr[x,y+1:] < arr[x,y]):
            vis[x,y] = 1
            continue
        
print(np.sum(np.sum(vis)))
            

#%% Part two: scenic score

scen = np.zeros_like(arr)
            

for x in range(size):
    
    visible = False

    for y in range(size):
        #edge cases are always 0
        if x == 0 or x == size-1 or y == 0 or y == size-1:
            scen[x,y]  = 0
            continue

        sup = 0
        for xx in range(x+1, size):
            if arr[xx,y] < arr[x,y]:
                sup += 1
            else:
                sup +=1
                break
        
        sdo = 0
        for xx in range(x-1, -1, -1):
            if arr[xx,y] < arr[x,y]:
                sdo += 1
            else:
                sdo +=1
                break
        
        sle = 0
        for yy in range(y-1,-1, -1):
            if arr[x,yy] < arr[x,y]:
                sle += 1
            else:
                sle +=1
                break

        sri = 0
        for yy in range(y+1, size):
            if arr[x,yy] < arr[x,y]:
                sri += 1
            else:
                sri +=1
                break
            
        scen[x,y] = sri*sdo*sup*sle
        
            
print(np.max(scen))
            