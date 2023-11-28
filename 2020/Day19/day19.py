#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: tobias

The solution of the second part is a bit on the "hardcoded" side and might 
not generalize. 
Although it solves my puzzle. 
Using the global variable in checking ig a solution is valod is not very elegant. 
"""

from itertools import product
from collections import Counter

with open("input.txt", "r") as f:    
    A = f.read()

rules, messages = A.split("\n\n")

rule_dict = {}

for rule in rules.split("\n"):
    number, instructions = rule.split(':')
    rule_dict[number] = {"matches":[], "possible_matches":None, "all_matches_found":False}
    instructions = instructions.split("|")
    for inst in instructions:
        rule_dict[number]["matches"].append(inst.split())
        
for rule in rule_dict.keys():
    if rule_dict[rule]["matches"] == [['"a"']]:
        rule_dict[rule]["possible_matches"] = {"a"}
        rule_dict[rule]["all_matches_found"] = True
    if rule_dict[rule]["matches"] == [['"b"']]:
        rule_dict[rule]["possible_matches"] = {"b"}
        rule_dict[rule]["all_matches_found"] = True
    
        

    
def rule_contains_only_letters(rule):
    x = "".join(rule)
    c = Counter(x)
    if len(x) == c["a"] + c["b"]:
        return True
    else:
        return False
    
# Identifying the rule chain
for i in range(7):
    for key in rule_dict.keys():
        if not rule_dict[key]["all_matches_found"]:
            
            all_rules = []
            for match in rule_dict[key]["matches"]:
                all_rules += match
            
            okay = True
            for rule in all_rules:
                if not rule_dict[rule]["all_matches_found"]:
                    okay = False
            
            if okay:
                possible_matches = set()
                for matches in rule_dict[key]["matches"]:
                    matches_set = []
                    for x in matches:
                        matches_set.append(rule_dict[x]["possible_matches"])

                    match_possible_matches = {"".join(combi) for combi in product(*matches_set)}
                    possible_matches = possible_matches.union(match_possible_matches)
                rule_dict[key]["possible_matches"] = possible_matches
                rule_dict[key]["all_matches_found"] = True
    
#%% Part 1

solution1 = sum([1 for message in messages.split('\n') if message in rule_dict["0"]["possible_matches"]])
print(f"Solution 1:\n{solution1}")        
    
#%% Part 2:
"""
Replace following rules:
8: 42
11: 42 31
with 
8: 42 | 42 8
11: 42 31 | 42 11 31

rule 8 and 11 contain themselves. 
Quick inspection of the input shows, that 8 and 11 are only called by 0. 

"""

min_len_8 = min([len(match) for match in rule_dict["8"]["possible_matches"]])
min_len_11 = min([len(match) for match in rule_dict["11"]["possible_matches"]])


matches_42 = rule_dict["42"]["possible_matches"]
matches_11 = rule_dict["11"]["possible_matches"] #the old rules
matches_31 = rule_dict["31"]["possible_matches"] 


def matches_rule_8(message):
    if len(message) == 0:
        return 
    
    if message[:8] in matches_42: #needs to start with some text which follows rule 8
        left_message = message[8:]
        
        matches_rule_8(left_message)
        matches_rule_11(left_message)

    
def matches_rule_11(message):
    global valid_message
    
    if len(message) == 0:
        return 
    
    elif len(message) == 16:
        if message in matches_11:
            valid_message = True
            
    elif len(message) == 32:
        c1 = message[:8] in matches_42
        c2 = message[8:16] in matches_42
        c3 = message[16:24] in matches_31
        c4 = message[24:] in matches_31
        
        if c1 and c2 and c3  and c4:
            valid_message = True
                
    elif len(message) == 48: 
        c1 = message[:8] in matches_42
        c2 = message[8:16] in matches_42
        c3 = message[16:24] in matches_42
        c4 = message[24:32] in matches_31
        c5 = message[32:40] in matches_31
        c6 = message[40:] in matches_31
        if c1 and c2 and c3  and c4 and c5 and c6:
            valid_message = True
    
    elif len(message) == 64: 
        c1 = message[:8] in matches_42
        c2 = message[8:16] in matches_42
        c3 = message[16:24] in matches_42
        c4 = message[24:32] in matches_42
        c5 = message[32:40] in matches_31
        c6 = message[40:48] in matches_31
        c7 = message[48:56] in matches_31
        c8 = message[56:] in matches_31
        if c1 and c2 and c3  and c4 and c5 and c6 and c7 and c8:
            valid_message = True
    

solution2 = 0 
for message in messages.split('\n'):
    left_message = message
    if not left_message[:8] in matches_42: #needs to start with some text which follows rule 8
        continue
    else:
        valid_message = False
        left_message = left_message[8:]
        matches_rule_8(left_message)
        matches_rule_11(left_message)
        
    if valid_message:
        solution2 += 1
        
print(f"Solution 2\n{solution2}")
        


    