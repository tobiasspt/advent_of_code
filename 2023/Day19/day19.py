#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import copy

##### Parsing the input
with open("input.txt", "r") as f:    
    A = f.read()
    
rules, parts = A.split("\n\n")

part_list = []
m = "m"
a = "a"
x = "x"
s = "s"
for part in parts.split("\n"):
    part = part.replace("=",":")
    part_list.append(eval(part))
    
rules_dict = {}
for rule in rules.split("\n"):
    name, instructions = rule.split("{")
    instructions = instructions.strip("}")
    instructions = instructions.split(",")
    
    instruction_list = []
    for inst in instructions[:-1]:
        condition, goto = inst.split(":")
        instruction_list.append((condition, goto))
        
    instruction_list.append(instructions[-1])
    rules_dict[name] = instruction_list
        
        
#### Part 1

def calculate_rating(part: dict) -> int:
    rating = 0
    for value in part.values():
        rating += value
    return rating


def handle_rule(part:dict, rule_name: str) -> int:
    
    if rule_name == "A":
        return calculate_rating(part)
    elif rule_name == "R":
        return None
    
    instructions = rules_dict[rule_name]
    for inst in instructions[:-1]:
        
        if "<" in inst[0]:
            prop, value = inst[0].split("<")
            value = int(value)
            if part[prop] < value:
                return handle_rule(part, inst[1])
            
        elif ">" in inst[0]:
            prop, value = inst[0].split(">")
            value = int(value)
            if part[prop] > value:
                return handle_rule(part, inst[1])
            
    return handle_rule(part, instructions[-1])
            

ratings = [handle_rule(part, "in") for part in part_list]
ratings = [x for x in ratings if x is not None]
res1 = sum(ratings)
print(f"Solution 1\n{res1}")
    

#%% Part 2




def handle_range(part_range: dict, rule_name: str) -> list[dict]:
    if rule_name == "A":
        return [part_range]
    
    elif rule_name == "R":
        return []
    
    accepted_ranges = []
    instructions = rules_dict[rule_name]
    for inst in instructions[:-1]:
        if "<" in inst[0]:
            prop, value_compared_to = inst[0].split("<")
            value_compared_to = int(value_compared_to)
            start, end = part_range[prop]
            
            if start >= value_compared_to: #None of the range applies to the rule
                continue
            if end < value_compared_to: 
                accepted_ranges += handle_range(part_range, inst[1]) # all of the range applies to the rule
            else:
                applying_range = copy.copy(part_range)
                applying_range[prop] = (start, value_compared_to-1)
                accepted_ranges += handle_range(applying_range, inst[1])
                part_range[prop] = (value_compared_to, end)
            

        elif ">" in inst[0]:
            prop, value_compared_to = inst[0].split(">")
            value_compared_to = int(value_compared_to)
            start, end = part_range[prop]
            
            if end <= value_compared_to: #None of the range applies to the rule
                continue
            if start > value_compared_to: 
                accepted_ranges += handle_range(part_range, inst[1]) # all of the range applies to the rule
            else:
                applying_range = copy.copy(part_range)
                applying_range[prop] = (value_compared_to+1, end)
                accepted_ranges += handle_range(applying_range, inst[1])
                part_range[prop] = (start, value_compared_to)
            
    # no conditions apply. follow the last instructions
    accepted_ranges += handle_range(part_range, instructions[-1])
    return accepted_ranges


def calulate_number_of_combinations(part_range: dict) -> int:
    number_of_ratings = 1
    for rang in part_range.values():
        s, e = rang
        number_of_ratings *= e-s+1
    return number_of_ratings
        

part_range = {"x":(1,4000), "m":(1,4000), "a":(1,4000), "s":(1,4000)}
all_allowed_ranges = handle_range(part_range, "in")
res2 = sum([calulate_number_of_combinations(part_range) for part_range in all_allowed_ranges])
print(f"Solution 2\n{res2}")
