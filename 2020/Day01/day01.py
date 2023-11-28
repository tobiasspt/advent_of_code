# -*- coding: utf-8 -*-

"""
Created on Thu Jan  6 16:59:15 2022

@author: spitaler.t
"""
import itertools
import numpy as np


with open("input.txt","r") as f:
    A = np.array(f.read().split('\n'), dtype=int) 


#Part 1
for i, j in itertools.product( range(len(A)-1), range(0,len(A))):
    if j <= i:
        continue

    if A[i] + A[j] == 2020:
        # print(A[i],A[j])
        res1 = A[i]*A[j]
        break
    
print(f"Solution1:\n{res1}")

#Part 2    
for i, j, k in itertools.product( range(len(A)-2), range(0,len(A)-1), range(0,len(A))):
    if j <= i:
        continue
    if k <= j:
        continue
    if A[i]+A[j]+A[k] == 2020:
        # print(A[i],A[j],A[k])
        res2 = A[i]*A[j]*A[k]
        break
print(f"Solution2:\n{res2}")
