#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
import numpy as np

def do_instruction(instruction: str, lights: np.ndarray) -> np.ndarray:
    w = instruction.split("through")
    x1, y1 = w[0].split()[-1].split(",")
    x2, y2 = w[-1].split(",")
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)+1
    y2 = int(y2)+1
    
    if "toggl" in instruction:
        lights[x1:x2, y1:y2] *= -1
    elif "on" in instruction:
        lights[x1:x2, y1:y2] = 1
    elif "off" in instruction:
        lights[x1:x2, y1:y2] = -1
    return lights


def do_instruction_2(instruction: str, lights: np.ndarray) -> np.ndarray:
    w = instruction.split("through")
    x1, y1 = w[0].split()[-1].split(",")
    x2, y2 = w[-1].split(",")
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)+1
    y2 = int(y2)+1
    
    if "toggl" in instruction:
        lights[x1:x2, y1:y2] += 2
    elif "on" in instruction:
        lights[x1:x2, y1:y2] += 1
    elif "off" in instruction:
        lights[x1:x2, y1:y2] -= 1
        lights[lights<0] = 0
    return lights


with open("input.txt", "r") as f:    
    A = f.read()    
instructions = A.split("\n")


## part 1
lights = np.ones([1000, 1000])*(-1)
for inst in instructions:
    lights = do_instruction(inst, lights)
res1 = np.sum(lights==1)
print("solution 1:", res1)


## part 2
lights = np.zeros([1000, 1000])
for inst in instructions:
    lights = do_instruction_2(inst, lights)
res2 = int(np.sum(lights))
print("solution 2:", res2)
