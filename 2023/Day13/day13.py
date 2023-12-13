#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import numpy as np
import copy

with open("input.txt", "r") as f:    
    A = f.read()


patterns_list = A.split("\n\n")
patterns_list = [np.array([list(line) for line in pattern.split("\n")]) for pattern in patterns_list]


def start_and_end(a, length):
    
    if a < length/2:
        first_start = 0
        last_end = 2*a
        
    else:
        last_end = length 
        first_start = 2*a- last_end 
        
    return first_start, last_end


def vertical_reflection(pattern: np.array) -> int:
    
    y_len = pattern.shape[1]
    for y in range(1, y_len):
        first_start, last_end = start_and_end(y, y_len)
        if np.all(pattern[:,first_start:y] == pattern[:, y:last_end][:,::-1]):
            return y
        
    # No mirror found
    return 0 


def horizontal_reflection(pattern: np.array) -> int:
    
    x_len = pattern.shape[0]
    for x in range(1, x_len):
        first_start, last_end = start_and_end(x, x_len)
        if np.all(pattern[first_start:x,:] == pattern[x:last_end][::-1,:]):
            return x
        
    # No mirror found
    return 0 
    


pattern_dict = dict() #needed for part 2

vrefs = []
hrefs = []
    
for i, pattern in enumerate(patterns_list):
    vref = vertical_reflection(pattern)
    href = horizontal_reflection(pattern)

    vrefs.append(vref)
    hrefs.append(href)
    
    # Needed for part 2
    if vref:
        pattern_dict[i] = ["v", vref]
    if href:
        pattern_dict[i] = ["h", href]
    
res1 = sum(vrefs) + sum(hrefs)*100
print(f"Solution 1\n{res1}")



#%% Part 2

def vertical_reflection_2(i: int, pattern: np.array) -> int:
    
    y_len = pattern.shape[1]
    for y in range(1, y_len):
        if pattern_dict[i] == ["v", y]:
            continue
        
        first_start, last_end = start_and_end(y, y_len)
        if np.all(pattern[:,first_start:y] == pattern[:, y:last_end][:,::-1]):
            return y
        
    # No mirror found
    return 0 


def horizontal_reflection_2(i: int, pattern: np.array) -> int:
    
    x_len = pattern.shape[0]
    for x in range(1, x_len):
        if pattern_dict[i] == ["h", x]:
            continue
        
        first_start, last_end = start_and_end(x, x_len)
        if np.all(pattern[first_start:x,:] == pattern[x:last_end][::-1,:]):
            return x
        
    # No mirror found
    return 0 



def pattern_smudge(i: int, pattern: np.array) -> (int, int):
    
    for x in range(pattern.shape[0]):
        for y in range(pattern.shape[1]): 
            new_pattern = copy.copy(pattern)
 
            if pattern[x,y] == ".":
                new_pattern[x,y] = "#"
                
            elif pattern[x,y] == "#":
                new_pattern[x,y] = "."
    

            vref = vertical_reflection_2(i, new_pattern)
            href = horizontal_reflection_2(i, new_pattern)
            
            if vref or href:
                return vref, href

    # No new mirrors found, should not happen
    return 0, 0


res2 = 0
for i, pattern in enumerate(patterns_list):
    vref, href = pattern_smudge(i, pattern)
    res2 += vref + 100*href
   
print(f"Solution 2\n{res2}")







