# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 07:36:07 2021

@author: spitaler.t
"""

import numpy as np
import copy

A = np.loadtxt('input.txt',delimiter=',', dtype=int)

fish = {}

for i,val in zip(range(len(A)),A): 
    fish[i] = val
    

counter = len(fish)

for i in range(80):
    
    c = copy.deepcopy(fish)
    for key,value in c.items():
        if value == 0:
            counter += 1
            fish[counter] = 8
            fish[key] =6
        else:
            fish[key] -=1
            
        
print(len(fish))


#%%
#Way smarter way to do it:
#2nd hopefully faster approach

tims = {}

for i in range(9):
    tims[i] = np.sum(A==i,dtype = float)
    
    
for i in range(256):
    
    foo = copy.deepcopy(tims)
    
    tims[0] = foo[1]
    tims[1] = foo[2]
    tims[2] = foo[3]
    tims[3] = foo[4]
    tims[4] = foo[5]
    tims[5] = foo[6]
    tims[6] = foo[7]+foo[0]
    tims[7] = foo[8]
    tims[8] = foo[0]

print(int(np.sum(list(tims.values()))))
#1639643057051
