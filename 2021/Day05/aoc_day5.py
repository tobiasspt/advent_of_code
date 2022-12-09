# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 09:17:42 2021

@author: spitaler.t
"""

import numpy as np


#%%
#reading in the lines

lines = {}
counter = 0

with open ('day5_input.txt') as file:
    line = file.readline().strip()

    while line and (line != ''):
    
        words = line.split()
        lines[counter] = np.zeros(4,dtype = int)
        
        lines[counter][:2] = words[0].split(',')
        lines[counter][2:] = words[2].split(',')    
        counter += 1
    
        line = file.readline().strip()


#%%

grid = np.zeros([1000,1000])

for line in lines.values():
    
    #same x
    if line[0] == line[2] and line[1] == line[3]:
        print('Poin-lines do exist')
    elif line[0] == line[2]:
        grid[line[0],min([line[1],line[3]]):max(line[1],line[3])+1] +=1
    
    #same y
    elif line[1] == line[3]:
        grid[min([line[0],line[2]]):max(line[0],line[2])+1,line[1]] +=1
    
res = np.sum(grid > 1)
print(res)


#%% 

#Now we need to consider as well diagonal lines

grid2 = np.zeros([1000,1000])

for line in lines.values():
    
    #same x
    if line[0] == line[2] and line[1] == line[3]:
        print('Poin-lines do exist')
    elif line[0] == line[2]:
        grid2[line[0],min([line[1],line[3]]):max(line[1],line[3])+1] +=1
    
    #same y
    elif line[1] == line[3]:
        grid2[min([line[0],line[2]]):max(line[0],line[2])+1,line[1]] +=1
        
    #diagonal lines
    # only 45 degrees
    else:
        
        if line[0] < line [2]:
            
            x_start = line[0]
            x_end = line[2]+1
            x_grow = True
            xrange = np.arange(x_start,x_end,1)
        else :
            x_start = line[0]
            x_end = line[2]-1
            x_grow = False
            xrange = np.arange(x_start,x_end,-1)
            
        if line[1] < line[3]:
            y_start = line[1]
            y_end = line[3]+1
            y_grow = True
            yrange = np.arange(y_start,y_end,1)
        else:
            y_start = line[1]
            y_end = line[3]-1
            y_grow = False           
            yrange = np.arange(y_start,y_end,-1)
            
        for x,y in zip(xrange,yrange):
            grid2[x,y]+=1
            
        
res = np.sum(grid2 > 1)
print(res)
