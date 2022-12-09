# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 07:22:34 2021

@author: spitaler.t
"""

import numpy as np


A = np.loadtxt('day13_input.txt',delimiter = ',')
# A = np.loadtxt('foo.txt',delimiter = ',')


B = """
fold along x=655
fold along y=447
fold along x=327
fold along y=223
fold along x=163
fold along y=111
fold along x=81
fold along y=55
fold along x=40
fold along y=27
fold along y=13
fold along y=6
"""

#%%
#Concentrate only on the first fold, how many are there points left? 

c1 = A.copy()

c1[:,0][c1[:,0]>655] = 655 - (c1[:,0][c1[:,0]>655] -655)

l = []

for i in range(c1.shape[0]):
    
    if list(c1[i,:]) not in l:
        l.append(list(c1[i,:]))
print(len(l))

#%%
#Fold all

c2 = A.copy()

for el in B.split('\n'):
    
    if el == '':
        continue

    w = el.split()[2]
    
    words = w.split('=')
    
    xy = words[0]
    num = int(words[1])

    if xy == 'x':
        ind = 0
    elif xy == 'y': 
        ind = 1
        

    c1[:,ind][c1[:,ind]>num] = num - (c1[:,ind][c1[:,ind]>num] -num)
    
    l = []
    
    for i in range(c1.shape[0]):
        
        if list(c1[i,:]) not in l:
            l.append(list(c1[i,:]))
   
    c1 = np.array(l)

import matplotlib.pyplot as plt
plt.figure(figsize =[15,2])
plt.plot(c1[:,0], -c1[:,1], '.', markersize=22)
print('PGHRKLKL')
