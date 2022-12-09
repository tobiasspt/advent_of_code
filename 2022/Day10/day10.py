# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np
import matplotlib.pyplot as plt


with open('input.txt', 'r') as f:
    A_input = f.read()
A = A_input.split('\n')

Xs = []
X = 1
for line in A:
    words = line.split()
    if words[0] == 'noop':
        Xs.append(X)
    elif words[0] == 'addx':
        Xs += [X,X]
        X+= int(words[1])
        
# Part 1
#Calculate the signal strenght
s_tot = 0
for i in range(20, 241, 40):
    s_tot += Xs[i-1]*i
print(s_tot)


##% part 2
X2 = np.array(Xs).reshape([6,40])
pixel_numbers = np.repeat(np.atleast_2d(np.arange(40)), 6, axis=0)
plt.imshow(np.abs(pixel_numbers-X2) <=1)



