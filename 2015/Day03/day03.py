#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

def deliver_presents(instructions: str) -> list[list[int,int]]:
    
    x = 0
    y = 0

    list_of_houses = [(x,y)]
    for d in instructions:
        
        if d == '^':
            y+= 1
        elif d == 'v':
            y-= 1
        elif d == '<':
            x-= 1
        elif d == '>':
            x += 1
           
        list_of_houses.append((x,y))

    return list_of_houses


with open("input.txt", "r") as f:    
    A = f.read()
instructions = list(A)


# part1
res1 = len(set(deliver_presents(instructions)))
print("Solution 1", res1)

res2 = len(set(deliver_presents(instructions[::2])+deliver_presents(instructions[1::2])))
print("Solution 2", res2)
