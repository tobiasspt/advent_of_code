#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
import numpy as np


def get_first_digit(line: list[str]) -> str:
    digits = [str(int(x)) for x in np.arange(1,10)]
    for l in line:
        if l in digits:
            return l

switches = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
repls = [str(x) for x in np.arange(1,10,1, dtype=int)]

def replace_front(line: str) -> str:
    indices = [line.find(s) if line.find(s) != -1 else 100 for s in switches]    
    if np.all(np.array(indices)==100):
        1==1
    else:
        change = np.argmin(indices)
        line = line.replace(switches[change], repls[change])
    return line

def replace_back(line: str) -> str:
    newline = line[::-1]
    indices = [newline.find(s[::-1]) if newline.find(s[::-1]) != -1 else 100 for s in switches]
    if np.all(np.array(indices)==100):
        1==1
    else:
        change = np.argmin(indices)
        newline = newline.replace(switches[change][::-1], repls[change])
    return newline

#%% Input reading
with open("input.txt", "r") as f:    
    A = f.read()
lines = A.split()


#%% Part 1
numbers = []
for line in lines:
    letters = list(line)
    num = get_first_digit(letters) +  get_first_digit(letters[::-1])
    numbers.append(int(num))
res1 = sum(numbers)
print(f"Solution 1:\n{res1}")


#%% Part 2
numbers = []
for line in lines:
   number = get_first_digit(replace_front(line)) + get_first_digit(replace_back(line))
   numbers.append(number)
res2 = sum([int(x) for x in numbers])
print(f"Solution 2:\n{res2}")



