#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
import itertools

with open("input.txt", "r") as f:    
    A = f.read()
containers = sorted([int(x) for x in A.split()])
eggnogg_ammount = 150

least_amount_variety = 0
n_combis = 0
for r in range(1, len(containers)+1):
    combis = itertools.combinations(containers, r)
    number_valid = sum([sum(combi)==eggnogg_ammount for combi in combis])
    if least_amount_variety == 0:
        least_amount_variety = number_valid
    n_combis += number_valid

print("Solution 1:", n_combis)
print("Solution 2:", least_amount_variety)