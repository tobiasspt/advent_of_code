#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

from cachetools import cached
from cachetools.keys import hashkey

def handle_pattern(pattern: str, score: int, towels: list[str], stop_success: bool=True) -> int:
    if stop_success:
        if score >= 1:
            return score
        
    if len(pattern) == 0:
        return  score + 1
    
    for tow in towels:
        if pattern.startswith(tow):
            score = handle_pattern(pattern[len(tow):], score, towels, stop_success)
    return score


@cached(cache={}, key=lambda pattern, towels: hashkey(pattern))
def handle_pattern_2(pattern: str, towels: list[str]):
    if len(pattern) == 0:
        return  1
    
    total_combis = 0
    for tow in towels:
        if pattern.startswith(tow):
            total_combis += handle_pattern_2(pattern[len(tow):], towels)
    return total_combis


## Input reading and parsing
with open("input.txt", "r") as f:    
    A = f.read()
towels, patterns = A.split("\n\n")
towels = towels.split(",")
towels = [x.strip() for x in towels]
patterns = patterns.split()

## Part 1
possible_patterns = [handle_pattern(pattern, 0, towels) for pattern in patterns]
res1 = sum(possible_patterns)
print("Solution 1:", res1)

## Part 2
number_combis = []
for pat in patterns:
    p_towels = [t for t in towels if t in pat]
    number_combis.append(handle_pattern_2(pat, p_towels))     
res2 = sum(number_combis)
print("Solution 2:", res2)

