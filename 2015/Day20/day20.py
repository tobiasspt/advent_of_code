#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import math
from functools import lru_cache

@lru_cache(maxsize=None)
def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor
        
@lru_cache(maxsize=None)
def get_all_divisor(n):
    return list(divisorGenerator(n))


with open("input.txt", "r") as f:    
    A = f.read()
min_presents = int(A)


##  part 1
house_number = 0
while True:
    house_number += 1
    divisors = get_all_divisor(house_number)
    presents = sum(divisors)*10
    if presents >= min_presents:
        break        
res1 = house_number
print("Solution 1:", house_number)


## part 2
house_number = 0
while True:
    house_number += 1
    min_number = house_number // 51 
    divisors = get_all_divisor(house_number)
    divisors = [x for x in divisors if x > min_number]
    presents = sum(divisors)*11
    if presents >= min_presents:
        break     
res2 = house_number
print("Solution 2:", res2)



