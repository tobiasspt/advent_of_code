# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np
import copy



with open('input.txt', 'r') as f:
    A_input = f.read()

pairs = []
for line in A_input.split('\n'):
    words = line.split(',')
    
    p = []
    for w in words:
        p.append([int(x) for x in w.split('-')])
    pairs.append(p)
    
    

total_overlapp = 0
for p in pairs:
    if p[0][0] <= p[1][0] and p[0][1] >= p[1][1]:
        total_overlapp+=1
    elif p[0][0] >= p[1][0] and p[0][1] <= p[1][1]:
        total_overlapp+=1
print(total_overlapp)
    

###part two

bit_overlapp = 0

for p in pairs: 
    if p[0][1] < p[1][0] or p[1][1] < p[0][0]:
        continue
    else:
        bit_overlapp +=1
            
print(bit_overlapp)
    
