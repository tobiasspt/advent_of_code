#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import numpy as np

def count_xmas_row(string: str) -> int:
    counter = 0
    if len(string) < 4:
        return counter
    for i in range(len(string)-3):
        check = string[i:i+4]
        if check in ["XMAS", "SAMX"]:
            counter += 1 
    return counter

def is_X_mas(pos: tuple[int,int], text: np.ndarray) -> bool:
    x,y = pos    
    b_diag1_1 =  text[x-1,y-1] == "M" and text[x+1,y+1] == "S"
    b_diag1_2 =  text[x-1,y-1] == "S" and text[x+1,y+1] == "M"
    
    b_diag2_1 =  text[x-1,y+1] == "M" and text[x+1,y-1] == "S"
    b_diag2_2 =  text[x-1,y+1] == "S" and text[x+1,y-1] == "M" 
    
    is_x = (b_diag1_1 or b_diag1_2) and (b_diag2_1 or b_diag2_2)
        
    if is_x:
        return True
    else:
        return False


with open("input.txt", "r") as f:    
    A = f.read()
text = np.array([list(x) for x in A.split("\n")], dtype=str)


## part 1
xmas_in_rows = 0
for i in range(text.shape[1]):
    string = "".join(text[:,i].tolist())
    xmas_in_rows += count_xmas_row(string)
    
xmas_in_cols = 0
for i in range(text.shape[0]):
    string = "".join(text[i,:].tolist())
    xmas_in_cols += count_xmas_row(string)

xmas_in_diag1 = 0
for i in range(-text.shape[0], text.shape[0]):
    string = "".join(np.diag(text, i).tolist())
    xmas_in_diag1 += count_xmas_row(string)

xmas_in_diag2 = 0
for i in range(-text.shape[0], text.shape[0]):
    string = "".join(np.diag(text[::-1,:], i).tolist())
    xmas_in_diag2 += count_xmas_row(string)
    
  
res1 = xmas_in_rows + xmas_in_cols + xmas_in_diag1 + xmas_in_diag2
print("Solution 1:", res1)

#%% part 2
x_mas_counter = 0
for x in range(1, text.shape[0]-1):
    for y in range(1, text.shape[0]-1):
        if text[x,y] == "A":
            if is_X_mas((x,y), text):
                x_mas_counter  += 1
print("Solution 2:", x_mas_counter)
    