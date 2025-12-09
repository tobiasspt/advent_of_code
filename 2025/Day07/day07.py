#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""


with open("input.txt", "r") as f:    
    A = f.read()
    
    
lines = A.split("\n")

## Part 1
number_splits = 0
beams = [0 if x == "."   else 1 for x in list(lines[0])]
for i, line in enumerate(lines[1:-1]):
    next_line = list(lines[i+1])
    new_beams = [0]*len(next_line)
    for li, beam in enumerate(beams):
        splitter = next_line[li]
        if beam and splitter == ".":
            new_beams[li] = 1
        elif beam and splitter ==  "^":
            new_beams[li] = 0
            new_beams[li+1] = 1
            new_beams[li-1] = 1
            number_splits += 1
    beams = new_beams
print(f"Solution 1: {number_splits}")


## Part 2, Quantum technology
beams = [0 if x == "."   else 1 for x in list(lines[0])]
for i, line in enumerate(lines[1:-1]):
    next_line = list(lines[i+1])
    new_beams = [0]*len(next_line)
    for li, beam in enumerate(beams):
        splitter = next_line[li]
        if beam and splitter == ".":
            new_beams[li] += beam
        elif beam and splitter ==  "^":
            new_beams[li] = 0
            new_beams[li+1] += beam
            new_beams[li-1] += beam
    beams = new_beams

number_timelines = sum(beams)#
print(f"Solution 2: {number_timelines}")