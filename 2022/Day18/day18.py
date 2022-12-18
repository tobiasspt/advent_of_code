# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np


# file = 'test.txt'
file = 'input.txt'

A_input = np.loadtxt(file, dtype=int, delimiter=',').tolist()
A_input = [tuple(x) for x in A_input]


def manhatten(pos1,pos2):
    return np.abs((pos1[0]-pos2[0])) + np.abs((pos1[1]-pos2[1])) + np.abs((pos1[2]-pos2[2]))

hidden_faces = 0
for i in range(len(A_input)-1):
    pos1 = A_input[i]
    for j in range(i, len(A_input)):
        pos2 = A_input[j]
        if manhatten(pos1, pos2) == 1:
            hidden_faces+=2
     
total_faces = len(A_input)*6
res1 = total_faces-hidden_faces
print('Part1 :', res1)
     

#%%

A_array = np.loadtxt(file, dtype=int, delimiter=',')

max_x = max(A_array[:,0])
max_y = max(A_array[:,1])
max_z = max(A_array[:,2])

    
free_air = set()

len_free_air_old = -1


while len(free_air) != len_free_air_old:
    new_free_air = set()
    
    for x in range(max_x+1):
        for y in range(max_y+1):
            for z in range(max_z+1):
    
                new_tuple = (x,y,z)
                
                if new_tuple not in A_input and new_tuple not in free_air:
                                    
                    #adding corners
                    if x == 0 and y == 0:
                        free_air.add(new_tuple)
                        continue
                    elif x == max_x and y == max_y:
                        free_air.add(new_tuple)
                        continue
                    elif x == 0 and z == 0:
                        free_air.add(new_tuple)
                        continue
                    elif x == max_x and z == max_z:
                        free_air.add(new_tuple)     
                        continue
                    if y == 0 and z == 0:
                        free_air.add(new_tuple)
                        continue
                    elif y == max_y and z == max_z:
                        free_air.add(new_tuple)    
                        continue
                    
                    for air_tuple in free_air:
                        if manhatten(new_tuple, air_tuple) == 1:
                            new_free_air.add(new_tuple)
                            break
                        
                   
    len_free_air_old = len(free_air)
    print(len(free_air))
    free_air = free_air.union(new_free_air)
                
    
# Finding the hidden air pockets:
hidden_air = []
for x in range(max_x+1):
    for y in range(max_y+1):
        for z in range(max_z+1):
            new_tuple = (x,y,z)
            if new_tuple not in A_input and new_tuple not in free_air:
                hidden_air.append(new_tuple)
                
    
hidden_faces_pockets = 0
for i in range(len(hidden_air)-1):
    pos1 = hidden_air[i]
    for j in range(i, len(hidden_air)):
        pos2 = hidden_air[j]
        if manhatten(pos1, pos2) == 1:
            hidden_faces_pockets+=2
     
total_faces_pockets = len(hidden_air)*6
outer_faces_pockets = total_faces_pockets-hidden_faces_pockets

res2 = res1 - outer_faces_pockets

print('Part 2:', res2)

                





