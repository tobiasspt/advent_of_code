#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

with open("input.txt", "r") as f:    
    A = f.read()


def edge_length(corners):
    length = 0
    for i in range(len(corners)-1):
        length += abs(corners[i][0] - corners[i+1][0]) + abs(corners[i][1] - corners[i+1][1])
    return length
    

def polygon_area(corners):
    "Shoelace formula"
    area = 0
    for i in range(len(corners)-1):
        area += 1/2*(corners[i+1][0]-corners[i][0])*(corners[i+1][1]+corners[i][1])
    return int(area + edge_length(corners)/2 +1)


     
lines = A.split("\n")

## Part 1
x = 0
y = 0
corners = [(x,y)]
for instruction in lines:
    
    direction, steps, color = instruction.split()
    steps = int(steps) 
    
    if direction == "U":
        x -= steps
    elif direction == "D":
        x += steps
    if direction == "L":
        y -= steps
    elif direction == "R":
        y += steps
        
    corners.append((x,y))

res1 = polygon_area(corners)
print(f"Solution 1\n{res1}")

### Part 2
x = 0
y = 0
corners = [(x,y)]

for instruction in lines:
    direction, _, color = instruction.split()
    color = color[1:-1]
    hexa = color[1:-1]
    steps = int(hexa,16)
    direction = color[-1]

    if direction == "3":
        x -= steps
    elif direction == "1":
        x += steps
    if direction == "2":
        y -= steps
    elif direction == "0":
        y += steps
    corners.append((x,y))

res2 = polygon_area(corners)
print(f"Solution 2\n{res2}")
