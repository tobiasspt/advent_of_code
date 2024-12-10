#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

def decode(eq_str: str) -> tuple[int, tuple[int,int]]:
    test_val, numbers = eq_str.split(":")
    test_val = int(test_val)
    numbers = [int(x) for x in numbers.split()]
    return (test_val, numbers)

def check_equation(val: int, numbers: list[int], test_val: int, check_val: int) -> bool:
    if len(numbers) == 0:
        if val == test_val:
            return check_val + 1
        else:
            return check_val 
    else:
        n_numbers = numbers[1:]
        n = numbers[0]
        check_val += check_equation(val*n, n_numbers, test_val, check_val)
        check_val += check_equation(val+n, n_numbers, test_val, check_val)
        return check_val

def check_equation_2(val: int, numbers: list[int], test_val: int, check_val: int) -> bool:
    if len(numbers) == 0:
        if val == test_val:
            return check_val + 1
        else:
            return check_val 
    else:
        n_numbers = numbers[1:]
        n = numbers[0]
        check_val += check_equation_2(val*n, n_numbers, test_val, check_val)
        check_val += check_equation_2(val+n, n_numbers, test_val, check_val)
        n_val = int(str(val)+str(n))
        check_val += check_equation_2(n_val, n_numbers, test_val, check_val)
        return check_val


with open("input.txt", "r") as f:    
    A = f.read()
eqs = A.split("\n")
eqs = [decode(eq_str) for eq_str in eqs]

## part 1
total_calibration_result = 0
eq_not_fullfilled = []
for i, eq in enumerate(eqs):
    test_val, numbers = eq
    if check_equation(numbers[0], numbers[1:], test_val, 0):
        total_calibration_result += test_val
    else:
        eq_not_fullfilled.append(eq)
print("Solution 1:", total_calibration_result)

## part 2
total_calibration_result_2 = total_calibration_result
for i, eq in enumerate(eq_not_fullfilled):
    test_val, numbers = eq
    if check_equation_2(numbers[0], numbers[1:], test_val, 0):
        total_calibration_result_2 += test_val
print("Solution 2:", total_calibration_result_2)



