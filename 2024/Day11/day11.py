#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
from functools import lru_cache

@lru_cache
def blink(number: int) -> list[int]:
    s = str(number) 
    ls = len(s)
    if number == 0:
        return [1]
    elif not len(s)%2:
        middle = int(ls/2)
        s1 = s[:middle]
        s2 = s[middle:]
        return [int(s1), int(s2)]
    else:
        return [number*2024]

@lru_cache(maxsize=None)  ## Fibonacci is that you?
def blink_for_n_times(n: int, number: int) -> int:
    if n == 1:
        return len(blink(number))
    else:
        n_tot = 0
        new_number = blink(number)
        for nn in new_number:
            n_tot += blink_for_n_times(n-1, nn)
        return n_tot
        
        
with open("input.txt", "r") as f:    
    A = f.read()
initial_numbers = [int(x) for x in A.split()]
    
res1 = sum([blink_for_n_times(25, number) for number in initial_numbers])
print("Solution 1:", res1)

res2 = sum([blink_for_n_times(75, number) for number in initial_numbers])
print("Solution 2:", res2)
