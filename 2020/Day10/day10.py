#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import numpy as np

with open("input.txt", "r") as f:    
    A = f.read()
    
adapters = np.array(A.split(), dtype=int)

adapters = np.sort(adapters)


n_three = np.sum(np.diff(adapters)==3) + 1 #add one for the last one
n_ones = np.sum(np.diff(adapters)==1) + 1 # add one for the first one, as it is one

solution1 = n_three*n_ones

print(f"Solution 1:\n{solution1}")


#%% Part 2

adapter_list = adapters.tolist() + [0, max(adapters)+3]
adapter_array  = np.array(adapter_list)
adapter_array = np.sort(adapter_array)
adapter_dict = {}

for adapter in adapter_list:
    possible_childs = adapter_array[np.logical_and(adapter_array-adapter>0, adapter_array-adapter<=3)]
    adapter_dict[adapter] = {"childs": possible_childs}

adapter_dict[max(adapter_list)]["possible_ways"] = 1

for adapter in adapter_array[-2::-1]:
    possible_ways = 0
    for child in adapter_dict[adapter]["childs"]:
        possible_ways += adapter_dict[child]["possible_ways"]
    adapter_dict[adapter]["possible_ways"] = possible_ways
    
solution2 = adapter_dict[0]["possible_ways"]
print(f"Solution 2:\n{solution2}")


    
    
