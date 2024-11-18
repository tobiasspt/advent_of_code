# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""


def merge_range_with_rule(valid: tuple[int, int], non_valid: tuple[int, int]) -> list[tuple[int, int]]:
    
    v_s, v_e = valid
    n_s, n_e = non_valid
    
    if v_s > n_e:
        return  [valid]
    elif v_e < n_s:
        return [valid]
    
    valid_ranges = []
    if v_s < n_s:
        valid_ranges.append((v_s, n_s-1))
    if v_e > n_e:
        valid_ranges.append((n_e+1, v_e))
    return valid_ranges
            

## reding input and finding the rules
with open("input.txt", 'r') as f:
    A = f.read()
rules = [x.split("-") for x in A.split("\n")]
excluded = [(int(x[0]),int(x[1])) for x in rules]        
max_ip = 4294967295

valid_ranges = [(0,max_ip)]

for rule in excluded:
    vr_list = []
    for vr in valid_ranges:
        vr_list += merge_range_with_rule(vr, rule)
    valid_ranges = vr_list
    
valid_ranges = sorted(valid_ranges, key=lambda x: x[0])

solution1 = valid_ranges[0][0]
print("Solution 1:", solution1)
            
#%% part 2

sum_valid_ranges = sum([x[1]-x[0]+1 for x in valid_ranges])
print("Solution 2:", sum_valid_ranges)

    
    