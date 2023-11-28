# -*- coding: utf-8 -*-

"""
Created on Thu Jan  6 20:10:21 2022

@author: spitaler.t
"""

with open("input.txt","r") as f:
    file = f.read()
    lines = file.split('\n')

number_lines = len(lines)


## Part 1
number_trees = 0
x_position = 0
y_position = 0
right_step = 3
line_lengt = len(lines[0])

for line in lines[1:]:    
    x_position += right_step
    if x_position > line_lengt-1: x_position -= line_lengt
    if line[x_position] == '#':
        number_trees += 1
    
print(f"Soution 1:\n{number_trees}")

#%%

step_x = [1,3,5,7,1]
step_y = [1,1,1,1,2]

number_trees_list = []

for xstep, ystep in zip(step_x, step_y):    
    number_trees = 0
    x_pos = 0
    y_pos = 0
    
    while True:    
        y_pos += ystep
        x_pos += xstep
        
        if y_pos >= number_lines: #reached the end
            break
        if x_pos > line_lengt-1: x_pos -= line_lengt
        if lines[y_pos][x_pos] == "#":
            number_trees += 1
    number_trees_list.append(number_trees)
        
      
product = 1
for x in number_trees_list:
    product*=x

print(f"Solution 2:\n{product}")

