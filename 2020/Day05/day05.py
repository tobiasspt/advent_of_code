#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: tobias
"""

import numpy as np

with open("input.txt", "r") as f:    
    A = f.read()
    passes = A.split()


def decode_pass(bpass: str) -> int:
    
    row_add = 2**np.arange(6,-1,-1)
    row_str = np.array(list(bpass[:7]))
    row = sum(row_add[row_str=='B'])
    
    col_add = 2**np.arange(2,-1,-1)
    col_str = np.array(list(bpass[7:]))
    col = sum(col_add[col_str=='R'])

    set_ID = row*8+col
    return set_ID


seat_IDs = [decode_pass(bpass) for bpass in passes]
print(f"Solution 1:\n {max(seat_IDs)}")


#%% part 2
possible_seats = []
for row in range(0,128):
    for col in range(8):
        possible_seats.append(row*8+col)
        
for seat in possible_seats:
    if seat not in seat_IDs and seat-1 in seat_IDs and seat+1 in seat_IDs:
        solution = seat
        break
        
print(f"Solution 2:\n{solution}")
