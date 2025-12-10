#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
from itertools import combinations
from functools import lru_cache
import numpy as np


def product(presents: list[int]) -> int:
    prod = 1
    for pres in presents:
        prod *= pres
    return prod

def get_combi_lengths(presents: list[int], target: int) -> bool:
    presents = sorted(presents)
    cum = np.cumsum(presents)
    cum_inv = np.cumsum(presents[::-1])
    ind_max = np.where(cum >= target)[0][0] 
    ind_min = np.where(cum_inv >= target)[0][0] + 1
    return ind_min, ind_max

@lru_cache(maxsize=None)
def can_be_split_equally(presents: list[int, int], target_weight: int) -> bool:
    ind_min, ind_max = get_combi_lengths(remaining_presents, target_weight)
    for rr in range(ind_min, ind_max+1):
        sub_combos = list(combinations(remaining_presents, rr))
        sub_combo_weights = [1 for x in sub_combos if sum(x) == target_weight]
        if sum(sub_combo_weights) > 0:
            return True
    return False


with open("input.txt", "r") as f:    
    A = f.read()
presents = [int(x) for x in A.split()]
total_weight = sum(presents)

## part 1
compartment_weight = total_weight/3
ind_min, ind_max = get_combi_lengths(presents, compartment_weight)
for n in range(ind_min, ind_max):
    allowed_combinations = []
    combis = list(combinations(presents, n))
    combis = [x for x in combis if sum(x) == compartment_weight]
    for candidate in combis:
        remaining_presents = sorted(list(set(presents) - set(candidate)))
        if can_be_split_equally(tuple(remaining_presents), compartment_weight):
            allowed_combinations.append(candidate)
            break
    if len(allowed_combinations) > 0:
        break
qes = [product(presents) for presents in allowed_combinations]
print("Solution 1:", min(qes))

## part 2
trunk_weight = total_weight//4
ind_min, ind_max = get_combi_lengths(presents, trunk_weight)
for n in range(ind_min, ind_max):
    allowed_combinations = []

    combis = list(combinations(presents, n))
    combis = [x for x in combis if sum(x) == trunk_weight]
    
    for candidate in combis:
        
        remaining_presents = sorted(list(set(presents) - set(candidate)))
        ind_min, ind_max = get_combi_lengths(remaining_presents, trunk_weight)
        found = False
        
        for rr in range(ind_min, ind_max+1):
            if found:
                break
            
            sub_combos = list(combinations(remaining_presents, rr))
            sub_combos = [x for x in sub_combos if sum(x) == trunk_weight]
            
            for candidate2 in sub_combos:
                if found:
                    break
                r_p_2 = sorted(list(set(remaining_presents)-set(candidate2)))
                if can_be_split_equally(tuple(r_p_2), trunk_weight):
                    allowed_combinations.append(candidate)
                    found = True
                    break

    if len(allowed_combinations) > 0:
        break
    
qes = [product(presents) for presents in allowed_combinations]
print("Solution 2:", min(qes))
