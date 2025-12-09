#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

with open("input.txt", "r") as f:    
    A = f.read()
    
## Part 1
pos = 50
n_0 = 0
for line in A.split("\n"):
    rot = line[0]
    amount = int(line[1:])
    if rot == "L":
        amount *= -1
    pos = (pos+amount)%100
    if pos == 0:
        n_0 += 1
print(f"Solution 1: {n_0}")


##Part 2
# Solution with 0-crossing counting

pos = 50
p2 = 50
n_0_clicks = 0
nums = []
for i, line in enumerate(A.split("\n")):
    rot = line[0]    
    
    amount = int(line[1:])
    if rot == "L":
        amount *= -1
        
    if pos == 0 and amount <0:
        n_0_clicks -= 1

    new_pos = pos + amount
    extra = abs( new_pos // 100 )
    n_0_clicks += extra

    pos  = new_pos % 100
    if new_pos == 0:
        n_0_clicks += 1
    if new_pos <0 and (abs(new_pos) % 100) == 0:
        n_0_clicks += 1
print(f"Solution 2: {n_0_clicks}")


## Part 2, "brute force" - solution
nums = []
pos = 50
for line  in A.split():
    rot = -1 if line[0] == "L" else 1
    amount = int(line[1:])
    for i in range(amount):
        pos = (pos + rot) % 100
        nums.append(pos)
res2 = sum([1 for x in nums if x == 0])
print(f"Solution 2: {res2}")


