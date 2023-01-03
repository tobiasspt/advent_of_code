# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np

# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:

    A_input = f.read()

chunks = A_input.split('\n\n')

instructions = chunks[-1]

board_map = chunks[0]


# Creating array of the input map
lines = board_map.split('\n')

max_x = max([len(line) for line in lines])

board_array = np.ones([len(lines), max_x], )*(-1)
for index, line  in enumerate(lines):
    
    line_array = np.array(list(line), dtype=str)
    
    empty_index = np.where(line_array == '.')
    wall_index = np.where(line_array == '#')
    board_array[index, empty_index] = 0
    board_array[index, wall_index] = 1
    
    
#Now comes the moving
y_start = 0 #moving up and down, first index
x_start = np.where(board_array[0,:] != -1)[0][0] #moving left right, second index


import re
forward_steps = re.findall(r"[0-9]{1,4}", instructions)
forward_steps = [int(x) for x in forward_steps]
turns  = re.findall(r"[R,L]", instructions)
    
# try:
int(instructions[0])
instructions_list = []
for i in range(len(forward_steps)):
    instructions_list.append(forward_steps[i])
    if i < len(turns):
        instructions_list.append(turns[i])  

x = x_start # moving right (+) and left (-), second index
y = y_start # moving up (-) and down (+), first index

orientation = 90 #clockwise
counter = 0

for inst in instructions_list:

    if inst == 'L':
       orientation = (orientation-90)%360
    elif inst == 'R':
        orientation = (orientation+90)%360
    
    else: #moving foreward
        
        if orientation == 0: #looking up
            dy = -1
            dx = 0
        elif orientation == 90:
            dy = 0
            dx = 1
        elif orientation == 180:
            dy = 1
            dx = 0
        elif orientation == 270:
            dy = 0
            dx = -1
            
        for step in range(inst):
            
            new_x = (x+dx)%max_x
            new_y = (y+dy)%len(lines)
            
            #Case of wrapping back
            if board_array[new_y, new_x] == -1:
                                
                y_indices = np.where(board_array[:, new_x] != -1)
                x_indices = np.where(board_array[new_y, :] != -1)
                
                if dy == 1:
                    new_y = y_indices[0][0]
                elif dy == -1:
                    new_y = y_indices[0][-1]
                elif dx == 1:
                    new_x = x_indices[0][0]
                elif dx == -1:
                    new_x = x_indices[0][-1]

            
            if board_array[new_y, new_x] == 0: #path is free. go
                1==1
                
            elif board_array[new_y, new_x] == 1: #hit a wall
                break
            
            x = new_x
            y = new_y
            
    
    counter += 1    
    

if orientation == 90:
    facing = 0
elif orientation == 180:
    facing = 1
elif orientation == 270:
    facing = 2
elif orientation == 0:
    facing = 3
    
print('Solution1:', facing + (y+1)*1000 + (x+1)*4)

        
        
    

        

        

    


