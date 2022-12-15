# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np


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


row = 2000000


slices = []

for sensor in sensors:
    dist = manhatten(*sensor)
    xs, ys, xb, yb = sensor   
    abs_xdist = dist - np.abs(ys-row)

    #does not block the row
    if abs_xdist < 0:
        continue
    else: 
        x1 = - abs_xdist + xs
        x2 = abs_xdist + xs
    
        slices += np.arange(min(x1,x2), max(x1,x2)+1).tolist()
     
# count present beacons and sensors?
sensors_in_row = []
for _, _, xb, yb in sensors:
    
    if yb == row:
        if [xb, yb] not in sensors_in_row:
            sensors_in_row.append([xb,yb])

        
print('Sol1:', len(np.unique(slices))-len(sensors_in_row))
    
