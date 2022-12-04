# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np
import copy


with open('input.txt', 'r') as f:
    A_input = f.read()


score  = 0

for line in A_input.split('\n'):
    
    
    me = line[-1]
    el = line[0]
    if me =='X':
        score += 1
        
        if el == 'A':
            score += 3
        elif el == 'C':
            score += 6

        
    elif me == 'Y':
        score += 2
    
        if el == 'A':
            score += 6
        elif el == 'B':
            score += 3
    
    elif me == 'Z':
        score += 3
        if el == 'C':
            score += 3
        elif el == 'B':
            score += 6

print(score)


#%%
score  = 0

for line in A_input.split('\n'):
    
    
    out = line[-1]
    el = line[0]
    
    
    
    if out =='X': #loose
    
        if el == 'A':
            score += 3
        elif el == 'B':
            score += 1
        elif el == 'C':
            score += 2
        
        
    elif out == 'Y':
        score  += 3
        
        if el == 'A':
            score += 1
        elif el == 'B':
            score += 2
        elif el == 'C':
            score += 3
        
    elif out == 'Z':
        score  += 6
        
        if el == 'A':
            score += 2
        elif el == 'B':
            score += 3
        elif el == 'C':
            score += 1
            
        


print(score)


    
