#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

def get_max_digit(bank_part: str) -> tuple[str, int]:
    for i in range(9,0,-1):
        if str(i) in bank_part:
            break
    index = bank_part.index(str(i))
    return str(i), index

def get_joltage_from_bank_with_override(bank: str, digits: int=2) -> int:
    
    joltage = ""
    for digit in range(digits):
        left = - (digits-1) + digit
        if left == 0:
            high_digit, index = get_max_digit(bank)
        else:
            high_digit, index = get_max_digit(bank[:left])
        
        joltage += high_digit
        if digit == (digits-1):
            continue
        bank = bank[index+1:]
    return int(joltage)


with open("input.txt", "r") as f:    
    A = f.read()
banks = A.split("\n")

## Part 1
res1 = sum([get_joltage_from_bank_with_override(bank, 2) for bank in banks])
print(f"Solution 1: {res1}")

## Part 2
res2 = sum([get_joltage_from_bank_with_override(bank, 12) for bank in banks])
print(f"Solution 2: {res2}")

