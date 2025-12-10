#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

def handle_line(line: str) -> [int, int]:
    storage_len = len(line)
    str_len = len(eval(line))
    return storage_len, str_len

def handle_line_2(line: str) -> [int, int]:
    str_len = len(line)
    storage_len = str_len + line.count('"') + line.count('\\') + 2
    return storage_len, str_len

## read input
with open("input.txt", "r") as f:    
    A = f.read()
lines = A.split("\n")

## part 1
lengths_1 = [handle_line(line) for line in lines]
res1 = sum([a-b for a,b in lengths_1])
print("Solution 1:", res1)

## part 2
lengths_2 = [handle_line_2(line) for line in lines]
res2 = sum([a-b for a,b in lengths_2])
print("Solution 2:", res2)
