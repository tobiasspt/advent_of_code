#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

def distance(box1: tuple[int,int,int], box2: tuple[int,int,int]) -> int:
    x1,y1,z1 = box1
    x2,y2,z2 = box2
    return (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
    

## Reading and parsing input
with open("input.txt", "r") as f:    
    A = f.read()
n_connections = 1000

junction_boxes = [tuple([int(y) for y in x.split(",")]) for x in A.split("\n")]
junction_boxes = sorted(junction_boxes)
distances = []
for i, box1 in enumerate(junction_boxes[:-1]):
    for box2 in junction_boxes[i+1:]:
        distances.append([box1, box2, distance(box1, box2)])
distances = sorted(distances, key=lambda x: x[2])


## Part 1
circuits = {}
c_added = 1

for i in range(n_connections):
    
    box1, box2, _ = distances[i]
    box1_c = 0
    box2_c = 0
   
    for ck in circuits.keys():
        if box1 in circuits[ck]:
            box1_c = ck
        if box2 in circuits[ck]:
            box2_c = ck
            
    if box1_c == 0 and box2_c == 0:
        circuits[c_added] = {box1, box2}
        c_added += 1
        continue
    
    if box1_c == 0:
        circuits[box2_c].add(box1)
    if box2_c == 0:
        circuits[box1_c].add(box2)
    if box1_c and box2_c:
        if box1_c == box2_c:
            continue
        
        circuits[box1_c] = circuits[box1_c].union(circuits[box2_c])
        del circuits[box2_c]

circuit_lengths = sorted(map(len, circuits.values()), reverse=True)
res1 = circuit_lengths[0]*circuit_lengths[1]*circuit_lengths[2]
print(f"Solution 1: {res1}")


### Part 2
circuits = {}
c_added = 1

i = 0
while True:
        
    box1, box2, _ = distances[i]
    i+= 1
   
    box1_c = 0
    box2_c = 0
   
    for ck in circuits.keys():
        if box1 in circuits[ck]:
            box1_c = ck
        if box2 in circuits[ck]:
            box2_c = ck
                
    if box1_c == 0 and box2_c == 0:
        circuits[c_added] = {box1, box2}
        c_added += 1
        continue
    
    if box1_c == 0:
        circuits[box2_c].add(box1)
    if box2_c == 0:
        circuits[box1_c].add(box2)

    if box1_c and box2_c:
        if box1_c == box2_c:
            continue
        
        circuits[box1_c] = circuits[box1_c].union(circuits[box2_c])
        del circuits[box2_c]
        
    
    if len(circuits[list(circuits.keys())[0]]) == len(junction_boxes):
        break
    
res2 = box1[0]*box2[0]
print(f"Solution 2: {res2}")