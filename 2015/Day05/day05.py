#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

def contains_at_least_3_vovel(s: str) -> bool:
    n_vowels = s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")
    return n_vowels >= 3

def contains_2_char_in_row(s: str) -> bool:
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False
    
def has_no_forbidden_str(s: str) -> bool:
    for forbidden_s in ["ab", "cd", "pq", "xy"]:
        if forbidden_s in s:
            return False
    return True

def is_nice(s: str) -> bool:
    return contains_2_char_in_row(s) and contains_at_least_3_vovel(s) and has_no_forbidden_str(s)



def contains_pair(s: str) -> bool:
    for i in range(len(s)-3):
        if s[i:i+2] in s[i+2:]:
            return True
    return False
    
def contains_repeated_letter(s: str) -> bool:
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            return True
    return False
    
def is_nice_2(s: str) -> bool:
    return contains_pair(s) and contains_repeated_letter(s)
    

with open("input.txt", "r") as f:    
    A = f.read()
strings = A.split("\n")

## part 1
res1 = sum([is_nice(s) for s in strings])
print("Solution 1:", res1)

## part 2
res2 = sum([is_nice_2(s) for s in strings])
print("Solution 2:", res2)



