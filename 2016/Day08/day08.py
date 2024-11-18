# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""
import matplotlib.pyplot as plt
import numpy as np


#scren: 50 pixels wide and 6 pixels tall
width = 50
tallness = 6


def rect(wide: int, tall: int, screen_array: np.ndarray) ->np.ndarray:
    screen_array[:tall, :wide] = 1
    return screen_array


def rotate_column(column_number: int, offset: int, screen_array: np.ndarray) -> np.ndarray:
    
    column = screen_array[:, column_number]
    
    indices = np.arange(tallness) - offset
    indices = indices%tallness
    
    screen_array[:, column_number] = column[indices]
    
    return screen_array
    
def rotate_row(row_number: int, offset: int, screen_array: np.ndarray) -> np.ndarray:
    
    column = screen_array[row_number, :]
    
    indices = np.arange(width) - offset
    indices = indices%width
    
    screen_array[row_number, :] = column[indices]
    
    return screen_array


#%% Part 1
#Reading the input
with open('input.txt','r') as f:    
    A = f.read()
instructions_list = A.split("\n")


screen_array = np.zeros([tallness, width])
for instruction in instructions_list:
    if "rect" in instruction:
        wide, tall = instruction.split()[1].split("x")
        wide = int(wide)
        tall = int(tall)
        screen_array = rect(wide, tall, screen_array)
        
    elif "column" in instruction:
        words = instruction.split()
        offset = int(words[-1])
        column_number = int(words[2].split("=")[-1])
        screen_array = rotate_column(column_number, offset, screen_array)
        
    elif "row" in instruction:
        words = instruction.split()
        offset = int(words[-1])
        row_number = int(words[2].split("=")[-1])
        screen_array = rotate_row(row_number, offset, screen_array) 
        
solution_1 = int(np.sum(np.sum(screen_array)))
print("Solution 1:", solution_1)

#%% Part 2
plt.imshow(screen_array)
plt.show()

