#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import numpy as np
import copy

with open("input.txt", "r") as f:    
    A = f.read()

histories = A.split("\n")
histories_list = [[int(x) for x in h.split()] for h in histories]
    
    
def find_next_value(history: list[int]) -> int:
    
    h_list = []
    h = copy.copy(history)
    h_list.append(h)
    
    while not np.all(np.array(h)==0):
        h = np.diff(h).tolist()
        h_list.append(h)

    n_histories = len(h_list)    
    h_list[-1].append(0)
    for i in range(n_histories-2, -1, -1):
        h_list[i].append(h_list[i][-1] + h_list[i+1][-1])

    return h_list[0][-1]    
    


next_vals = [find_next_value(h) for h in histories_list]    
res1 = sum(next_vals)
print(f"Solution 1\n{res1}")
    

next_vals2 = [find_next_value(h[::-1]) for h in histories_list]
res2 = sum(next_vals2)
print(f"Solution 2\n{res2}")
    
    
    
    
    
    
    
    
    
    
    