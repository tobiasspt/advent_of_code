#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: tobias
"""

import numpy as np

with open("input.txt", "r") as f:    
    A = f.read()


A = np.loadtxt("input.txt", dtype=int)
list1 = np.sort(A[:,0])
list2 = np.sort(A[:,1])
total_distance = np.sum(np.abs(list1-list2))

print("Solution 1:", total_distance)

#%% part 2, similarity  score
right_list = list2.tolist()
similarity_score = sum([i*right_list.count(i) for i in list1])
print("The similarity score is:", similarity_score)


