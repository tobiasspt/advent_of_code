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
    
int(instructions[0])
instructions_list = []
for i in range(len(forward_steps)):
    instructions_list.append(forward_steps[i])
    if i < len(turns):
        instructions_list.append(turns[i])  


#%% Constructing an boarder map by hand, with which I can work

board_array2 = board_array.copy()

board_array2[150:,50:100] = board_array[150:,:50].transpose()[-1::-1, :]
board_array2[150:, :50] = -1

board_array2[100:150,100:] = board_array[:50,100:][-1::-1,-1::-1]
board_array2[:50:, 100:] = -1


faces_dict = {}

cube_len = 50

for y in range(0, len(lines)//cube_len):
    for x in range(0, max_x//cube_len):        
        if board_array2[y*cube_len,x*cube_len] != -1:
            faces_dict[(y*cube_len,x*cube_len)] = {'up':None, 'down':None, 'left': None, 'right': None}

#%%

def move(instructions, y_start, x_start, orientation):

    x = x_start
    y = y_start
    orientation = orientation        
    instructions_list = instructions

    counter = 0
    
    for inst in instructions_list:    
    
    
        if inst == 'L':
            orientation = (orientation-90)%360
        elif inst == 'R':
            orientation = (orientation+90)%360
        
        else: #moving foreward
            for step in range(inst):
                
                assert board_array2[y,x] != 1
                assert board_array2[y,x] != -1
                
                
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
                
                
                new_x = x+dx
                new_y = (y+dy)%len(lines)
                

                new_orientation = orientation
                
                # print(new_x)
                resx = new_x%cube_len
                resy = new_y%cube_len  
    
                # case, when the x goes out of the bounds
                if (new_x <0) or (new_x >= max_x):
                    
                    if new_x < 0:
                        new_y = 49 - resy 
                        new_x = 50
                        
                        new_orientation = 90        
                        
                    elif new_x >= max_x:
    
                        new_y = 49 - resy                    
                        new_x = 99
                        
                        new_orientation = 270
    
                    
                elif  board_array2[new_y, new_x] == -1:
                        
                        if (100 <= new_x < max_x) and ( 100 <= y < 150):
                            
                            
                            
                            if orientation == 0:
                                new_y = 99 - resx
                                new_x = 99
                                new_orientation = 270

                                
                            elif orientation == 180:
                                new_y = 150 + resx
                                new_x = 99
                                new_orientation = 270
                  
                        elif (0 <= new_x < 50) and ( 100 <= y < 150):
                            if orientation == 0:
                                new_y = 50 + resx
                                new_x = 50
                                new_orientation = 90                           
                                
                            elif orientation == 180:
                                new_y = 150 + (49 - resx)
                                new_x = 50
                                new_orientation = 90              
                        
                        elif 150 <= new_y < 200 and ( 50 <= x < 100):
                            if orientation == 90:
                                new_x = 100 + resy
                                new_y = 149 
                                new_orientation = 0

                                
                            elif orientation == 270:
                                new_x = 49 - resy
                                new_y = 149
                                new_orientation = 0

                                
                        elif (50 <= new_y < 100) and  ( 50 <= x < 100):
                            if orientation == 90:
                                new_x = 100 + (49 - resy) 
                                new_y = 100
                                new_orientation = 180


                            elif orientation == 270:
                                new_x = resy
                                new_y = 100
                                new_orientation = 180
                                
                                
                        elif (0 <= new_y < 50) and ( 50 <= x < 100):
                            
                            # print('here')
                            if orientation == 90:
                                new_y = 149 - resy
                                new_x = 149
                                new_orientation = 270
                                
                            elif orientation == 270:
                                new_y = 149 - resy
                                new_x = 0
                                new_orientation = 90
                                

                assert board_array2[new_y, new_x] != -1         
                
                if board_array2[new_y, new_x] == 0: #path is free. go
                    1==1
                    
                elif board_array2[new_y, new_x] == 1: #hit a wall
                    break
                
                x = new_x
                y = new_y
                orientation = new_orientation
        
        counter += 1    
    
    return x, y, orientation


x = x_start # moving right (+) and left (-), second index
y = y_start # moving up (-) and down (+), first index

orientation = 90 #clockwise

x, y, orientation = move(instructions_list, y_start, x_start, orientation)


#In my case mapping back
orientation  = (orientation-180)%360

#Because i did change the original map, the final position might be in an area
# which changed comparing to the original input. Therefore I have to map back. 

original_map = np.zeros([200,150])
original_map[y,x] = 1

original_map[:50, 100:] =  original_map[100:150,100:][-1::-1, -1::-1]
original_map[100:150,100:] = 0

original_map[150:, :50] = original_map[150:,50:100].transpose()[-1::-1, :]
original_map[150:,50:100] = 0

xx = np.where(original_map)

y_correct = xx[0][0]
x_correct = xx[1][0]


if orientation == 90:
    facing = 0
elif orientation == 180:
    facing = 1
elif orientation == 270:
    facing = 2
elif orientation == 0:
    facing = 3
    
print('Solution2:', facing + (y_correct+1)*1000 + (x_correct+1)*4)


        
