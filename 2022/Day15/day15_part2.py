# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np
from collections import defaultdict
from itertools import chain


with open('input.txt', 'r') as f:
    A_input = f.read()

sensors = []
for line in A_input.split('\n'):
    words = line.split()
    
    xs = int(words[2].strip('x=').strip(','))
    ys = int(words[3].strip('y=').strip(':'))
    xb = int(words[8].strip('x=').strip(','))
    yb = int(words[9].strip('y=').strip(':'))
    
    sensors.append([xs, ys, xb, yb])


def manhatten(x1, y1, x2, y2):
    return np.abs(x1-x2) + np.abs(y1-y2)


    
#%% Part two

rmin = 0
rmax = 4000000


# dictionary containtng for each row the ranges which are blocked by the 
# sensors
dic = defaultdict(lambda: [])

#Fillwing this dictionary takes ~ 2 min
for sensor in sensors:
    
    dist = manhatten(*sensor)
    xs, ys, xb, yb = sensor   
    
    row_min = ys - dist
    row_max = ys + dist
    
    for row in range(max(row_min,0), min(row_max, rmax)+1):
        abs_xdist = dist - np.abs(ys-row)

        x1 = - abs_xdist + xs
        x2 = abs_xdist + xs
            
        start = max(min(x1,x2), rmin)
        end = min(max(x1,x2), rmax)
    
        dic[row].append([start, end])
    

#%%
    
def check_ranges(ranges):
    """
    Returns True if there is no empty spot.
    Else False
    """
    rsorted = sorted(ranges, key = lambda x: x[0])    
        
    mini = rsorted[0][0]
    if mini != 0:
        return False
    maxi = rsorted[0][1]
    
    for r in rsorted[1:]:
        s,e = r
        if s > maxi+1:
            return False
        else:
            if e > maxi:
                maxi = e
        
    if maxi != rmax:
        return False
    return True


#%%

#Looping over the rows, to find the row, where there is the empty spot
# Takes only ~10 sec. Is not the bottle neck.
for row in range(len(dic)):
    if not check_ranges(dic[row]):
        print(row)
        break
    
# Cumbersome way of determining the column value
setis = []
for r in dic[row]:
    setis.append(range(r[0],r[1]+1))

in_row = set(chain(*setis))
whole_range = set(range(rmax+1))
set_diff = whole_range-in_row
column = list(set_diff)[0]
   
print('Sol2:', column*4000000+row)

