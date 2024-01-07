#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import numpy as np

with open("input.txt", "r") as f:    
    A = f.read()


def get_xage(universe: np.ndarray, age: int) -> np.ndarray:
    x_age = np.zeros_like(universe, dtype=int)
    for i in range(universe.shape[0]):        
        if np.sum(universe[i,:] =="#") == 0:
            x_age[i,:] = age -1
    return x_age
    
    
def get_yage(universe: np.ndarray, age: int) -> np.ndarray:
    y_age = np.zeros_like(universe, dtype=int)
    for i in range(universe.shape[1]):
        if np.sum(universe[:,i] =="#") == 0:
            y_age[:,i] = age -1
    return y_age


def total_distances(universe: np.ndarray, age: int) -> int:
    x_age = get_xage(universe, age)
    y_age = get_yage(universe, age)
    
    indices = np.where(universe == "#")
    xind = indices[0]
    yind = indices[1]
    
    total_distances = 0

    for i in range(len(xind)-1):
        x1 = xind[i]
        y1 = yind[i]
        
        for j in range(i+1,len(xind)):
            x2 = xind[j]
            y2 = yind[j]
            dist = np.abs(x1-x2) + np.abs(y2-y1) 
            xage_extra =  sum(x_age[min(x1,x2):max(x1,x2), 0])
            yage_extra =  sum(y_age[0,min(y1,y2):max(y1,y2)])
            dist += xage_extra + yage_extra
            total_distances += dist
            
    return total_distances
            

lines = A.split("\n")
universe = np.array([list(line) for line in lines])

res1 = total_distances(universe, 2)
print(f"Solution 1:\n{res1}")

res2 = res1 = total_distances(universe, 1000000)
print(f"Solution 2:\n{res2}")

    
    