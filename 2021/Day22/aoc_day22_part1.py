# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 09:11:16 2021

@author: spitaler.t
"""

import numpy as np

A = np.zeros([101,101,101])

s = 50

file = 'day22_input.txt'

line = ' '
with open(file) as f:
    
    while line: 
        line = f.readline()
        
        if line != '':
            
            words = line.split()
            
            onoff = words[0]
            
            words = words[1].split(',')
            
            X = words[0].split('..')
            xa = int(X[0][2:])
            xe = int(X[1])
            
            Y = words[1].split('..')
            ya = int(Y[0][2:])
            ye = int(Y[1])
            
            Z = words[2].split('..')
            za = int(Z[0][2:])
            ze = int(Z[1])
        
            #shift the coordinates
            
            xa+= 50
            xe+= 50
            
            ya += 50
            ye += 50
            
            za += 50
            ze += 50
        
            
            if xa > 101 or xa < 0:
                continue
            if onoff == 'on':
                A[xa:xe+1,ya:ye+1,za:ze+1] = 1
            elif onoff == 'off':
                A[xa:xe+1,ya:ye+1,za:ze+1] = 0
                
print(np.sum(A==1))

    

