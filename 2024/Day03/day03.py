#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: tobias
"""

import matplotlib.pyplot as plt
import numpy as np
import copy
import re

with open("input.txt", "r") as f:    
    A = f.read()

def multiply(multxt):
    w = multxt.split("(")[1][:-1].split(",")
    return int(w[0])*int(w[1])


multis = re.findall("mul\(\d+,\d+\)", A)
result1 = sum([multiply(multxt) for multxt in multis])
print("Solution 1: ", result1)

#%% part2


list2 = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", A)

multis2 = []

do = True
for x in list2:
    if x == "do()":
        do = True
    elif x == "don't()":
        do = False
    else:
        if do:
            multis2.append(x)
    
result2 = sum([multiply(multxt) for multxt in multis2])
print("Solution 2: ", result2)