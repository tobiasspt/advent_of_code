#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

def get_prizes(claw_machine: list[tuple[int,int]], extra_distance: int=0) ->list[int]:
    """
    m * xA + n * xB = Px
    m * yA + n * yB = Py
    """

    bA, bB, prize = claw_machine
    
    xA, yA = bA
    xB, yB = bB
    px, py = prize
    px += extra_distance
    py += extra_distance
    
    m_numerator  = px*yB - py*xB
    m_denominator = xA*yB - yA*xB
    if m_numerator % m_denominator:
        return []
    m = m_numerator // m_denominator
    if m < 0:
        return []
    
    n_numerator = py - m * yA
    n_denominator = yB
    if n_numerator % n_denominator:
        return []
    n = n_numerator // n_denominator
    if n < 0:
        return []

    return [3*m + 1*n]
    

## loading and parsing input
with open("input.txt", "r") as f:    
    A = f.read()
claw_machines = A.split("\n\n")
claw_machine_dict = {}
for i,cm in enumerate(claw_machines):
    bA, bB, prize = cm.split("\n")
    bA = [int(x.split("+")[-1]) for x in  bA.split(":")[-1].split(",")]
    bB = [int(x.split("+")[-1]) for x in  bB.split(":")[-1].split(",")]
    prize = [int(x.split("=")[-1]) for x in  prize.split(":")[-1].split(",")]
    claw_machine_dict[i] = (bA, bB, prize)

## part 1
prizes_list = [get_prizes(claw_machine_dict[key]) for key in claw_machine_dict.keys() ]
res1 = sum(min(p) for p in prizes_list if len(p) >0)
print("Solution 1:", res1)
    
## part 2
extra_distance = 10000000000000
prizes_list_2 = [get_prizes(claw_machine_dict[key], extra_distance) for key in claw_machine_dict.keys() ]
res2 = sum(min(p) for p in prizes_list_2 if len(p) >0)
print("Solution 2:", res2)




