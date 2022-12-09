# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

from collections import Counter

with open('input.txt', 'r') as f:
    A_input = f.read()
buffer = list(A_input)

def find_start_of(buffer, length):   
    for i in range(len(buffer)-4):
        if len(list(Counter(buffer[i:i+length]).keys())) ==length:
            return i + length
    
print(find_start_of(buffer, 4))
print(find_start_of(buffer, 14))


    
    
    