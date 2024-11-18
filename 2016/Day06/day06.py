# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""

#Reading the input
with open('input.txt','r') as f:    
    A = f.read()
    

def most_frequent(List):
    #Source: https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
    return max(set(List), key=List.count)

def least_freqent(List):
    return min(set(List), key=List.count)

signal_list = [list(x) for x in A.split("\n")]

solution_1 = ""
for i in range(len(signal_list[0])):
    column = [x[i] for x in signal_list]
    solution_1 += most_frequent(column)

print("Solution 1", solution_1)


solution_2 = ""
for i in range(len(signal_list[0])):
    column = [x[i] for x in signal_list]
    solution_2 += least_freqent(column)

print("Solution 2", solution_2)


