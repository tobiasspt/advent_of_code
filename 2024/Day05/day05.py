#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import copy


def obays_rule(rule: tuple[int,int], update: list[int]) -> bool:
    n1, n2 = rule
    if n1 in update and n2 in update:
        if update.index(n1) < update.index(n2):
            return True
        else:
            return False
    else:
        return True

def is_update_correct(update: list[int], rules: list[tuple[int,int]]) -> bool:
    if len(update) == 1:
        return True
    for rule in rules:
        if not obays_rule(rule, update):
            return False
    return True

def get_active_rules(update: list[int], rules: list[tuple[int,int]]) -> [list[tuple[int,int]], int]:
    applying_rules = []
    for rule in rules: 
        n1, n2 = rule
        if n1 in update and n2 in update:
            applying_rules.append(rule)
        
    numbers_in_rules = [] 
    for r in applying_rules:
        numbers_in_rules += list(r) 
    numbers_in_rules = set(numbers_in_rules)

    return applying_rules, numbers_in_rules

def find_correct_update_order(update: list[int], rules: list[tuple[int,int]]) -> list[int]:
    active_rules, numbers_in_rules = get_active_rules(update, rules)
        
    numbers_to_add = copy.copy(numbers_in_rules)
    correct_order = [numbers_to_add.pop()]
    while len(numbers_to_add) > 0:
        nn  = numbers_to_add.pop()
        for i in range(len(correct_order)+1):
            new_order = copy.copy(correct_order)
            new_order.insert(i, nn)
            if is_update_correct(new_order, active_rules):
                correct_order = new_order
                break
    
    assert len(correct_order) == len(update), (correct_order, update)
    return correct_order


## Reading and parsing input
with open("input.txt", "r") as f:    
    A = f.read()
rules, updates = A.split("\n\n")
rules = [(int(x.split("|")[0]), int(x.split("|")[1])) for x in rules.split()]
updates = [ [ int(x) for x in update.split(",")] for update in updates.split("\n")]


# part 1
middle_number_sum = 0
for update in updates:
    if is_update_correct(update, rules):
        middle_number_sum += update[int(len(update)/2)]
print("Solution 1:", middle_number_sum)


# part 2: find the correct ordering
middle_number_sum_2 = 0
for update in updates:
    if not is_update_correct(update, rules):
        correct_update = find_correct_update_order(update, rules)
        middle_number_sum_2 += correct_update[int(len(update)/2)]
print("Solution 1:", middle_number_sum_2)



    
    


