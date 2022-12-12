# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np
import copy
from collections import defaultdict



with open('input.txt', 'r') as f:
    A_input = f.read()

l = []
for line in A_input.split('\n'):
    l.append([ord(x) for x in list(line)])
A = np.array(l)


start = np.where(A==ord('S'))
end = np.where(A==ord('E'))

x_start = start[0][0]
y_start = start[1][0]

x_end = end[0][0]
y_end = end[1][0]

A[x_start, y_start] = 1000
A[x_end, y_end] = 0

lenx = A.shape[0]
leny = A.shape[1]

def pos_to_str(X):
    return str(X[0])+'|'+str(X[1])

def str_to_pos(pstr):
    w = pstr.split('|')
    return [int(w[0]), int(w[1])]
    
def pathlen(path):
    return len(path.split('/'))

unexplored = defaultdict(lambda: {'path':None})
unexplored[pos_to_str([x_start, y_start])] = {'path':'start'}

explored = defaultdict(lambda: {'path':None})

while len(unexplored) > 0:
    
    for u in list(unexplored.keys()):
        
        parent_path = unexplored[u]['path']
        
        X = str_to_pos(u)
        x = X[0]
        y = X[1]
                
        candidates = []
        #candidate position check outside of border
        if x-1 >= 0:
            candidates.append([x-1, y])
        if x+1 < lenx:
            candidates.append([x+1, y])
        if y-1 >= 0:
            candidates.append([x, y-1])
        if y+1 < leny:
            candidates.append([x, y+1])

        #Filter candidates for jump hight limitation
        candidates = [c for c in candidates if (A[c[0],[c[1]]] - A[x,y])  < 2 ]
        
        # now a check if the path is shorter as before
        for c in candidates:
            newpath = parent_path + '/' + pos_to_str(c)
            
            #newpath is in the unexplored list, check if new route is shorter
            if pos_to_str(c) in list(unexplored.keys()):
                if pathlen(newpath) < pathlen(unexplored[pos_to_str(c)]['path']):
                    unexplored[pos_to_str(c)]['path'] = newpath
            
            #newpath is in the explored list, check if new route is shorter
            elif pos_to_str(c) in list(explored.keys()):
                if pathlen(newpath) < pathlen(explored[pos_to_str(c)]['path']):
                    unexplored[pos_to_str(c)]['path'] = newpath
                    del explored[pos_to_str(c)]
                    
            else:
                unexplored[pos_to_str(c)]['path']  = newpath
        
        explored[u]['path'] = parent_path
        del unexplored[u]        
        

endstr = pos_to_str([x_end,y_end])
print(pathlen(explored[endstr]['path'])-1)


#%%
#Plotting of part 1

import matplotlib.pyplot as plt
heatmap = np.zeros_like(A) 
for u in explored: 
    X = str_to_pos(u)
    x = X[0]
    y = X[1] 
    heatmap[x,y] = pathlen(explored[u]['path'])

plt.figure(dpi=200)
plt.title('Number steps to rach from S to the position')
plt.imshow(heatmap)
plt.plot([y_start], [x_start], 'rx', label='S')
plt.plot([y_end], [x_end], 'r.', label='End')
plt.legend()
plt.colorbar()


#%% Par two
print('Part two takes several minutes!')

#where are the a?
a_pos = np.where(A == ord('a'))

steps = []

endstr = pos_to_str([x_end,y_end])


for xx,yy,i in zip(a_pos[0], a_pos[1], range(len(a_pos[0]))):  

    # unexplored = defaultdict(lambda: {'path':None})
    unexplored = {}
    unexplored[pos_to_str([xx, yy])] = {'path':pos_to_str([xx,yy])}
    
    # explored = defaultdict(lambda: {'path':None})
    explored = {}
    
    while len(unexplored) > 0:
        
        for u in list(unexplored.keys()):
            parent_path = unexplored[u]['path']
            
            X = str_to_pos(u)
            x = X[0]
            y = X[1]
                    
            candidates = []
            #candidate position check outside of border
            if x-1 >= 0:
                candidates.append([x-1, y])
            if x+1 < lenx:
                candidates.append([x+1, y])
            if y-1 >= 0:
                candidates.append([x, y-1])
            if y+1 < leny:
                candidates.append([x, y+1])
    
            # filter possible moves (hight-jump-limit)
            candidates = [c for c in candidates if (A[c[0],[c[1]]] - A[x,y])  < 2 ]

            for c in candidates:
                newpath = parent_path + '/' + pos_to_str(c)
                   
                #newpath is in the unexplored list, check if new route is shorter
                if pos_to_str(c) in list(unexplored.keys()):
                    if pathlen(newpath) < pathlen(unexplored[pos_to_str(c)]['path']):
                        unexplored[pos_to_str(c)]['path'] = newpath
                
                #newpath is in the explored list, check if new route is shorter
                elif pos_to_str(c) in list(explored.keys()):
                    if pathlen(newpath) < pathlen(explored[pos_to_str(c)]['path']):
                        unexplored[pos_to_str(c)]['path'] = newpath
                        del explored[pos_to_str(c)]
                
                #add to unexplored    
                else:
                    unexplored[pos_to_str(c)] = {'path': newpath}
            
            explored[u] = {'path': parent_path}
            del unexplored[u]        
            
    #There are batches of a which one can not climb out without taking a stephigh
    # of two or more
    try:
        steps.append(pathlen(explored[endstr]['path'])-1)
    except:
        steps.append(np.nan)

print(int(np.nanmin(steps)))    


