# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 07:48:46 2021

@author: spitaler.t
"""

import numpy as np
import matplotlib.pyplot as plt

grid = np.zeros([100,100])

with open('day9_input.txt') as file:
    for i in range(100):
        line = file.readline()
        grid[i,:] = list(line.split()[0])
           
#%%

risk = 0
cords = []
for i in range(100):
    
    for j in range(100):
        
        num = grid[i,j]
        
        b1,b2,b3,b4 = True,True,True, True
        
        if i > 0:         
            b1 = grid[i-1,j] > num
        if j > 0:
            b2 = grid[i,j-1] > num
        if i < 99:
            b3 = grid[i+1,j] > num
        if j < 99:
            b4 = grid[i,j+1] > num

        if b1 and b2 and b3 and b4:
            
            risk += num+1
            cords.append([i,j])
print(int(risk))

#%%

basinsize = []
counter = 0

g = grid.copy()    
    
for x in range(100):
    for y in range(100):
        
        num = g[x,y]
        
        if num < 9:
            
            cord_search = [[x-1,y],[x,y-1],[x+1,y],[x,y+1]]
            cord_search_done = []
            bsize = 1
            
            g[x,y] = 10
             
            #check all the proposed cords
            while len(cord_search) > 0:
                
                foo = cord_search[0]
                xs,ys = foo
                
                if foo in cord_search_done:
                    cord_search.remove(foo)
                    
                
                elif xs < 0 or ys < 0 or xs > 99 or ys > 99:
                    cord_search_done.append(foo)
                    cord_search.remove(foo)
                
                elif g[xs,ys] < 9:
                    bsize += 1
                    g[xs,ys] = 10
                    
                    cord_search.append([xs-1,ys])
                    cord_search.append([xs,ys-1])
                    cord_search.append([xs+1,ys])
                    cord_search.append([xs,ys+1])
                    cord_search.remove(foo)
                    cord_search_done.append(foo)
                    
                elif g[xs,ys] >=9:
                    cord_search.remove(foo)
                    cord_search_done.append(foo)
                    
                    
            basinsize.append(bsize)
            
a = np.sort(basinsize)
res2 = a[-1]*a[-2]*a[-3]
print(res2)
            
            
            
        


