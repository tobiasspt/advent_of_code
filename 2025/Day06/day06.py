#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
import math


def cephalopods_math(nums: list[int], symbol: str) -> int:
    if symbol == "+":
        res = sum(nums)
    if symbol == "*":
        res = math.prod(nums)
    return res
    

with open("input.txt", "r") as f:    
    A = f.read()

## Part 1
grid = [x.split() for x in A.split("\n")]

solutions = []
for i in range(len(grid[0])):
    nums = list(map(int, (grid[x][i] for x in range(4))))
    symbol = grid[4][i]
    solutions.append(cephalopods_math(nums, symbol))
    
res1 = sum(solutions)
print(f"Solution 1: {res1}")


## Part 2
grid_2 = [list(x) for x in A.split("\n")]
indices = []
for i, char in enumerate(grid_2[-1]):
    if char in ["*","+"]:
       indices.append(i)

def get_nums(i2: int, i1: int) -> list[int]:
    nums = []
    for aa in range(i2-i1-1):
        n = ""
        for _x in range(4):
            n += grid_2[_x][i1+aa]
        nums.append(int(n))
    return nums

solutions = []
for _i in range(len(indices)-1):
    i1 = indices[_i]
    i2 = indices[_i+1]
    nums = get_nums(i2, i1)
    symbol = grid_2[-1][i1]
    solutions.append(cephalopods_math(nums, symbol))

## Add the last number
i1 = indices[-1]
nums = get_nums(len(grid_2[0])+1, i1)
symbol = grid_2[-1][i1]
solutions.append(cephalopods_math(nums, symbol))

res2 = sum(solutions)
print(f"Solution 2: {res2}")