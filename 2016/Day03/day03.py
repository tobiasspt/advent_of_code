# -*- coding: utf-8 -*-
"""

@author: spitaler.t
"""
import numpy as np

#Reading the input
with open('input.txt','r') as f:    
    A = f.read()


## Part 1
triangles_list = A.split("\n")
triangles_arrays = [np.array(tri.split(), dtype=int) for tri in triangles_list]


def triangle_check(triangle: np.ndarray[int]) -> bool:
    
    sorted_nums = np.sort(triangle)
    if sorted_nums[0] + sorted_nums[1] > sorted_nums[2]:
        return True
    else:
        return False
    

valid_trianlges = 0
for triangle in triangles_arrays:
    if  triangle_check(triangle):
        valid_trianlges += 1
print("Solution 1:", valid_trianlges)
       
#%%
##Part2
numbers_array = np.loadtxt("input.txt")

nr_size = numbers_array.shape
new_length = max(nr_size)*3
numbers_array = np.reshape(numbers_array, [new_length], order="F" )

triangles_arrays_2 = np.reshape(numbers_array, nr_size)

valid_trianlges_2 = 0
for triangle in triangles_arrays_2:
    if  triangle_check(triangle):
        valid_trianlges_2 += 1
print("Solution 2:", valid_trianlges_2)