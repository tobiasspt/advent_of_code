# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np
import copy


with open('input.txt', 'r') as f:
    A_input = f.read()

elves_list = A_input.split('\n\n')


#dictionary of the elves
d = {}
for i in range(len(elves_list)):
    d[i] = np.sum(np.array(elves_list[i].split('\n'), dtype=int))
print(np.max(list(d.values())))

#%%
elves = list(d.values())
elves = np.sort(elves)
print(np.sum(elves[-3:]))


