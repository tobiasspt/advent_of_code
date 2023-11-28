#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import numpy as np


with open("input.txt", "r") as f:    
    A = f.read()

instructions = A.split()

"""
N = 0 degrees
E = 90 degrees
S = 180 degrees
W = 270 degrees

negative x is west, positive x is east
negative y is south, positive y is north
"""

face = 90 # starting east
posx = 0
posy = 0


for inst in instructions:
    
    act = inst[0]
    value = int(inst[1:])
    
    
    if act == "N": 
        posy += value
    elif act == "E":
        posx += value
    elif act == "S":
        posy -= value
    elif act == "W":
        posx -= value
    elif act == "R":
        face += value
        face = face%360
    elif act == "L":
        face -= value
        face = face%360
    elif act == "F":
        if face == 0:
            posy += value
        elif face == 90:
            posx += value
        elif face == 180:
            posy -= value
        elif face == 270:
            posx -= value
            
solution1 = abs(posx) + abs(posy)
print(f"Solution 1:\n{solution1}")
                    

#%% Part 2
posx = 0
posy = 0

wposx = 10
wposy = 1

for inst in instructions:
    act = inst[0]
    value = int(inst[1:])
    
    if act == "N": 
        wposy += value
    elif act == "E":
        wposx += value
    elif act == "S":
        wposy -= value
    elif act == "W":
        wposx -= value
         
    elif act in ["R", "L"]: 
        r2 = np.sqrt(wposx**2 + wposy**2)
        phi = np.arctan2(wposy, wposx)
        if act == "R":
            phi_new = phi - value/360*2*np.pi
        elif act == "L":
            phi_new = phi + value/360*2*np.pi
        phi_new = phi_new%(2*np.pi)
        cosphi = np.cos(phi_new)
        sinphi = np.sin(phi_new)
        wposy = np.round(sinphi*r2)
        wposx = np.round(cosphi*r2)
    
    elif act == "F":
        posx += value * wposx
        posy += value * wposy
        
solution2 = abs(posx) + abs(posy)
print(f"Solution 2:\n{int(solution2)}")


