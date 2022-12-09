# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np
import copy



with open('input.txt', 'r') as f:
    A_input = f.read()

motions =  A_input.split('\n')

def is_adjecent(hx,hy,tx,ty):
    
    dist = np.sqrt((hx-tx)**2 + (hy-ty)**2)
    if dist > np.sqrt(2):
        return False
    else:
        return True
    

def follow(hx, hy, tx, ty):
    
    if not is_adjecent(hx, hy, tx, ty):
        if hx == tx:
            ty += np.sign(hy-ty)
        elif hy == ty:
            tx += np.sign(hx-tx)
            
        
        #folow diagonally
        elif np.abs(hx-tx) > 1 and np.abs(hy-ty) > 1:
            ty += np.sign(hy-ty)
            tx += np.sign(hx-tx)
      
        else: #"Semi-" Diagonal moove 
            if np.abs(hx - tx) >  1:
                tx = hx - np.sign(hx-tx)
                ty = hy
            elif np.abs(hy-ty) > 1:
                ty = hy -np.sign(hy-ty)
                tx = hx
            
    return tx, ty


#%% Part 1
t_visists = []


hx = 0
hy = 0

tx = 0
ty = 0


for m in motions:
    words = m.split()
    
    if words[0] == 'U':
        
        for i in range(int(words[1])):
            hy += 1
        
            tx, ty = follow(hx, hy, tx, ty)
            if [tx,ty] not in t_visists:
                t_visists.append([tx,ty])
        
            if not is_adjecent(hx, hy, tx, ty):
                print('wtf')
                3/0
        
    elif words[0] == 'D':
            
        for i in range(int(words[1])):
            hy -= 1
            
            tx, ty = follow(hx, hy, tx, ty)
            if [tx,ty] not in t_visists:
                t_visists.append([tx,ty])
 
            if not is_adjecent(hx, hy, tx, ty):
                print('wtf')
                3/0
                    
            
    elif words[0] == 'R':
        
        for i in range(int(words[1])):
            hx += 1
            
            tx, ty = follow(hx, hy, tx, ty)
            if [tx,ty] not in t_visists:
                t_visists.append([tx,ty])

            if not is_adjecent(hx, hy, tx, ty):
                print('wtf')
                3/0
        
    elif words[0] == 'L':
            
        for i in range(int(words[1])):
            hx -= 1        

            tx, ty = follow(hx, hy, tx, ty)
            if [tx,ty] not in t_visists:
                t_visists.append([tx,ty])

            if not is_adjecent(hx, hy, tx, ty):
                print('wtf')
                3/0

                
print(len(t_visists))

#%% Part two


x_nots = np.array([0,0,0,0,0,0,0,0,0,0])
y_nots = np.array([0,0,0,0,0,0,0,0,0,0])

t_visits = []

for m in motions:
    words = m.split()
    
    if words[0] == 'U':
        
        for i in range(int(words[1])):
            y_nots[0] += 1
        
            for i in range(9):
                tx, ty = follow(x_nots[i], y_nots[i], x_nots[i+1], y_nots[i+1])
                x_nots[i+1] = tx
                y_nots[i+1] = ty
                
            if [x_nots[-1], y_nots[-1]] not in t_visits:
                t_visits.append([x_nots[-1], y_nots[-1]])
        

    elif words[0] == 'D':
            
        for i in range(int(words[1])):
            y_nots[0] -= 1
            
            for i in range(9):
                tx, ty = follow(x_nots[i], y_nots[i], x_nots[i+1], y_nots[i+1])
                x_nots[i+1] = tx
                y_nots[i+1] = ty
                
            if [x_nots[-1], y_nots[-1]] not in t_visits:
                t_visits.append([x_nots[-1], y_nots[-1]])

            
    elif words[0] == 'R':
        
        for i in range(int(words[1])):
            x_nots[0] += 1
            
            for i in range(9):
                tx, ty = follow(x_nots[i], y_nots[i], x_nots[i+1], y_nots[i+1])
                x_nots[i+1] = tx
                y_nots[i+1] = ty
                
            if [x_nots[-1], y_nots[-1]] not in t_visits:
                t_visits.append([x_nots[-1], y_nots[-1]])
        
        
    elif words[0] == 'L':
            
        for i in range(int(words[1])):
            x_nots[0] -= 1
            
            for i in range(9):
                tx, ty = follow(x_nots[i], y_nots[i], x_nots[i+1], y_nots[i+1])
                x_nots[i+1] = tx
                y_nots[i+1] = ty
                
            if [x_nots[-1], y_nots[-1]] not in t_visits:
                t_visits.append([x_nots[-1], y_nots[-1]])

print(len(t_visits))
