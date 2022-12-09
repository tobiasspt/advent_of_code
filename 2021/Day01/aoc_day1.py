# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
nums = np.loadtxt('input.txt')

res = np.sum(np.diff(nums)>0)
print(res)

#%% 3 measurment sliding window
mw = np.zeros(len(nums)-2)

mw += nums[:-2]
mw += nums[1:-1]
mw += nums[2:]

res2 = np.sum(np.diff(mw)>0)
print(res2)