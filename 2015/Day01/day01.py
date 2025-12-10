# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:23:03 2022

@author: spitaler.t
"""


with open("input.txt") as f:
    A = f.read()

res = A.count('(') - A.count(')')
print("Soution 1: ", res)


#%% part 2, basement entering

i = 0
pos = 0

while True :
    if A[i] == '(':
        pos += 1
    elif A[i] == ')':
        pos -= 1
        
    i +=1
    
    if pos == -1:
        res2 = i
        break
    
print("Solution 2:", res2)