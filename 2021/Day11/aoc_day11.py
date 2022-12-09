# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 08:06:55 2021

@author: spitaler.t
"""

import numpy as np

with open('input.txt','r') as f:
    A_input = f.read().split('\n')
    
A = []
for line in A_input:
    A.append(list(line))
A = np.array(A, dtype=int)


flashed_tot = 0
B = A.copy()

it = 100
for s in range(it):    
    flashed = B < -100

    # everyone gets +1
    B+=1
    
    #if there is any flashable octopus, let them flash!
    while np.any(B>9):
        
        #looping over the array
        for i in range(10):
            for j in range(10):
                if B[i,j] > 9 and not flashed[i,j]:
                    
                    flashed[i,j] = True
                    B[i,j] = -1
                    
                    for xx in [-1,0,1]:
                        x = i+xx
                        
                        for yy in [-1,0,1]:     
                            y = j+yy
                            if x >= 0 and x < 10 and y >=0 and y < 10 and B[x,y] != -1:
                                
                                B[x,y]+=1

                    
    B[B<0] = 0
    flashed_tot+= np.sum(flashed)
    
print(flashed_tot)
# print(B)      
               

    
#%% Part 2

flashed_tot = 0
B = A.copy()

it = 1000
for s in range(it):
    flashed = B < -100
    # everyone gets +1
    B+=1
    #if there is any flashable octopus, let them flash!
    while np.any(B>9):
 
        #looping over the array
        for i in range(10):
            for j in range(10):
                if B[i,j] > 9 and not flashed[i,j]:
                    
                    flashed[i,j] = True
                    B[i,j] = -1
                    
                    for xx in [-1,0,1]:
                        x = i+xx
                        
                        for yy in [-1,0,1]:     
                            y = j+yy
                            if x >= 0 and x < 10 and y >=0 and y < 10 and B[x,y] != -1:
                                
                                # print(x,y)
                                B[x,y]+=1

                    
    B[B<0] = 0
    flashed_tot+= np.sum(flashed)
    
    if np.all(flashed):
        break
print(s+1)

               
    