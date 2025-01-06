#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

def count_pins(lock: str) -> list[int]:
    lines = lock.split("\n")
    pins = [-1,-1,-1,-1,-1]
    for line in lines:
        pins = [s+1 if c == "#" else s for s,c in zip(pins,list(line))]
    return pins

def match(lock: list[int], key: list[int]) -> bool:
    max_pin_sum = 5
    sums = [l+k for l,k in zip(lock, key)]
    return not sum([1 if s > max_pin_sum else 0 for s in sums])
    

## Reading and parsing input
with open("input.txt", "r") as f:    
    A = f.read()
schematics = A.split("\n\n")
locks = [s for s in schematics if s.startswith("#####")]
keys = [s for s in schematics if s.endswith("#####")]

## Finding pin hights
lock_pins = [count_pins(lock) for lock in locks]
key_pins = [count_pins(key) for key in keys]

## Counting valid key-lock combinations
fit_together = 0
for lp in lock_pins:
    for kp in key_pins:
        if match(lp, kp):
            fit_together += 1
            
print("Solution: ", fit_together)

