#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

def sum_from_1_to_n(n: int) -> int:
    return n*(n+1)//2

def first_column(row: int) -> int:
    return sum_from_1_to_n(row-1) + 1
    
def calc_code_number(row: int, column: int) -> int:
    fc = first_column(row)   
    return fc + sum_from_1_to_n(column+row-1) - sum_from_1_to_n(row)

with open("input.txt", "r") as f:    
    A = f.read()
words = A.split()
row = int(words[-3][:-1])
column = int(words[-1][:-1])
code_number = calc_code_number(row, column)
    
code_one = 20151125
multi = 252533
divider = 33554393

code = code_one
for i in range(code_number-1):
    code = ( code * multi ) % divider
print("Solution:", code)
