#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

with open("input.txt", "r") as f:    
    A = f.read()

ranges = [[int(x) for x in y.split("-")] for y in A.split(",")]

def valid_id(pid: int) -> bool: 
    spid = str(pid)
    ## uneven cant be a sequenze
    if len(spid) % 2: 
        return True
    halflen = int(len(spid) / 2)
    if spid[:halflen] == spid[halflen:]:
        return False
    else:
        return True
    
def valid_id_2(pid: int) -> bool:
    """
    Returns False if the product_id (pid) is not valid
    """
    spid = str(pid)
    spidlen = len(spid)
    for i in range(1, int(spidlen/2)+1):
        if spidlen % i:
            continue
        test_str = spid[:i] * (spidlen // i)
        if test_str == spid:
            return False
    return True
        

## Part 1
invalid_ids = []
for id_range in ranges:
    lower, upper = id_range
    invalid_ids += [pid for pid in range(lower, upper+1) if not valid_id(pid)]
res1 = sum(invalid_ids)
print(f"Solution 1: {res1}")


## Part 2
invalid_ids2 = []
for id_range in ranges:
    lower, upper = id_range
    invalid_ids2 += [pid for pid in range(lower, upper+1) if not valid_id_2(pid)]
res2 = sum(invalid_ids2)
print(f"Solution 2: {res2}")


