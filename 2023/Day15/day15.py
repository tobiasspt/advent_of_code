#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""


with open("input.txt", "r") as f:    
    A = f.read()
steps = A.split(",")


def get_hash(step: str):
    current_value = 0
    for char in step:
        current_value = ((current_value + ord(char))*17) % 256
    return current_value

res1 = sum( [get_hash(x) for x in steps])
print(f"Solution 1\n{res1}")


#%% Part 2

box_dict = dict()
for i in range(256):
    box_dict[i] = []

for step in steps:
    
    if "-" in step:
        label, _ = step.split("-")
        boxnum = get_hash(label)
        for lense in box_dict[boxnum]:
            if label in lense:
                box_dict[boxnum].remove(lense)
                break

        
    elif "=" in step:
        label, focal_length = step.split("=")
        boxnum = get_hash(label)
        is_in = False
        for lense in box_dict[boxnum]:
            if label in lense:
                is_in = True
                alread_in_lense = lense
                break
        if not is_in:
            box_dict[boxnum].append([label, focal_length])
        else:
            index = box_dict[boxnum].index(alread_in_lense)
            box_dict[boxnum].insert(index, [label, focal_length])
            box_dict[boxnum].remove(alread_in_lense)
            

def calculate_total_focusing_power(box_dict):
    total_focusing_power = 0
    for box in box_dict.keys():
        focusing_power = (box+1) * sum([(i+1)*int(x[1]) for i,x in enumerate(box_dict[box])])
        total_focusing_power += focusing_power
    return total_focusing_power

print(f"Solution 2\n{calculate_total_focusing_power(box_dict)}")













