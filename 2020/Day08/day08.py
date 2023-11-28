#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import copy

with open("input.txt", "r") as f:    
    A = f.read()


# A = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6"""


instructions = A.split("\n")

#Part one
acc = 0
pos_list = []
pos = 0

while pos not in pos_list:
    pos_list.append(pos)
    instruction = instructions[pos].split()
    action = instruction[0]
    value = int(instruction[1])
    if action == "nop":
        pos += 1
    elif action == "acc":
        acc += value
        pos+=1
    elif action == "jmp":
        pos+=value
        
print(f"Solution 1:\n{acc}")
    
#%% Part two

def run_program(inst_new: list[str]):
    
    acc = 0
    pos_list = []
    pos = 0

    while pos not in pos_list:
        pos_list.append(pos)
        instruction = inst_new[pos].split()
        action = instruction[0]
        value = int(instruction[1])
        if action == "nop":
            pos += 1
        elif action == "acc":
            acc += value
            pos+=1
        elif action == "jmp":
            pos+=value
    
        if pos == len(inst_new): #programm terminated succesfully
            return acc
        
    return None # programm not terminated sucessfull



for i, instruction in enumerate(instructions):
    
    action = instruction.split()[0]
    value = int(instruction.split()[1])    
    if action == "acc":
        continue
    
    inst_new = copy.deepcopy(instructions)
    
    if action == "nop":
        inst_new[i] = "jmp "+str(value)
    elif action == "jmp":
        inst_new[i] = "nop "+str(value)
    
    solution2 = run_program(inst_new)
    
    print(i, solution2)
    
    if solution2 is not None:
        break
    
print(solution2)





    