#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: tobias
"""

import numpy as np
import copy

with open("input.txt", "r") as f:    
    A = f.read()

rules, myticket, othertickets = A.split('\n\n')


#%% Part 1
allowed_ranges = []

for rule in rules.split('\n'):
    text, values = rule.split(':')
    ranges = values.split(' or ')
    for r in ranges:
        mi, ma = r.split('-')
        allowed_ranges.append((int(mi),int(ma)))
    
def is_in_range(num: int) -> bool:
    for r in allowed_ranges:
        if r[0] <= num <= r[1]:
            return True
    return False

ticket_scanning_error_rate = 0
for ticket in othertickets.split('\n')[1:]:
    nums = np.array(ticket.split(','), dtype=int)
    ticket_scanning_error_rate += sum([x for x in nums if not is_in_range(x)])
    
print(f"Solution 1:\n{ticket_scanning_error_rate}")
    
#%% Part 2
# Identify which ticket is which

myticket_nums = np.array(myticket.split('\n')[1].split(','), dtype=int)

# get all the valid tickets
valid_tickets = []
for ticket in othertickets.split('\n')[1:]:
    nums = np.array(ticket.split(','), dtype=int)
    tser = 0
    tser += sum([x for x in nums if not is_in_range(x)])
    if tser == 0:
        valid_tickets.append(nums)


rules_dict = {}
for rule in rules.split('\n'):
    text, values = rule.split(':')
    ranges = values.split(' or ')
    rule_r = []
    for r in ranges:
        mi, ma = r.split('-')
        rule_r.append((int(mi),int(ma)))
    rules_dict[text] = {"r":rule_r, "possible_positions":[]}
    
    
def valid_for_rule(nums: np.array(int), rule) -> bool:
    # Gives true if an array of numbers fullfills the rule. Otherwise False
    rule_r = rules_dict[rule]["r"]
    for num in nums:
        in_range = False
        for r in rule_r:
            if r[0] <= num <= r[1]:
                in_range = True
                continue
        if not in_range:
            return False
    return True
        

#Checking for every position in the tickets which rule they could obey
for position in range(20):
    position_nums = np.array([x[position] for x in valid_tickets])
    for rule in rules_dict.keys():
        if valid_for_rule(position_nums, rule):
            rules_dict[rule]["possible_positions"].append(position)
        
    
# Finding out which rule the numbers actually obey. If there is only one 
# Possible position which obeys to a rule, this position can not be at another 
# rule 
rules_dict_solution = copy.deepcopy(rules_dict)
counter = 0

while True: 
    for rule in rules_dict_solution.keys():
        if len(rules_dict_solution[rule]["possible_positions"]) == 1:
            fixed_pos = rules_dict_solution[rule]["possible_positions"][0]
            rules_dict_solution[rule]["fixed_position"] = fixed_pos
            for rule in rules_dict_solution.keys():
                try:
                    rules_dict_solution[rule]["possible_positions"].remove(fixed_pos)
                except: # avoid error, when fixed_pos is not in the list
                        1==1
            break
    counter += 1
    if counter >=30:
        break
        
    
# calculating th actual solution
departure_product = 1.0
for rule in rules_dict_solution.keys():
    if "departure" in rule:
        departure_product *= myticket_nums[rules_dict_solution[rule]["fixed_position"]]
print(f"Solution 2:\n{int(departure_product)}")
