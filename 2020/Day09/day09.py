#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import numpy as np
import itertools

with open("input.txt", "r") as f:    
    A = f.read()

numbers = np.array(A.split(), dtype=float).round()

N = 25 #preamble length

#%% Part 1

def check_validity(n, prev_numbers ):
    valid = False
    for j,k in itertools.product(range(N-1), range(N)):
        if k <= j:
            continue
        else:
            if prev_numbers[j]+prev_numbers[k] == n:
                valid = True
    return valid

pos = N+1
while True:
    valid = check_validity(numbers[pos], numbers[pos-N:pos])
    if not valid:
        solution1 = numbers[pos]
        break
    pos+=1

print(f"Solution 1:\n{round(solution1)}")     
        
#%% Part 2

for i1 in range(1000):
    cumsum = np.cumsum(numbers[i1:])
    if np.any(cumsum==solution1):
        i2 = np.where(cumsum==solution1)[0][0]
        i2 += i1 + 1
        break
        
solution2 = max(numbers[i1:i2] + min(numbers[i1:i2]))
print(f"Solution 2:\n{round(solution2)}")     


