# -*- coding: utf-8 -*-

"""
Created on Thu Jan  6 18:30:42 2022

@author: spitaler.t
"""

import numpy as np


line = 'x'


valid_counter = 0

with open('input.txt') as f:
    while line:
        line = f.readline()
        if line != '':
            words = line.strip().split()
            nums = np.array(words[0].split('-'),dtype = int)
            let = words[1][:-1]
            pasw = np.array(list(words[2]),dtype = str)
            if nums[0] <= np.sum(pasw==let) <= nums[1]:
                valid_counter+=1
print(f"Solution 1:\n{valid_counter}")

#%%
#part 2

line = 'x'

valid_counter2 = 0

with open('input.txt') as f:
    while line:
        line = f.readline()
        if line != '':
            words = line.strip().split()
            nums = np.array(words[0].split('-'),dtype = int)
            let = words[1][:-1]
            pasw = np.array(list(words[2]),dtype = str)
            foo = 0
            if pasw[nums[0]-1] == let: foo +=1
            if pasw[nums[1]-1] == let: foo +=1
            if foo == 1:
                valid_counter2 += 1
print(f"Solution 1:\n{valid_counter2}")
