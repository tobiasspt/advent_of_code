# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np
import copy

with open("input.txt") as f:
    A = f.read()
    stacks_str, A_input = A.split("\n\n")
    

stacks = {}
for i in range(1,10):
    stacks[i] = []


indices_of_letters = list(range(1,1+9*4,4))
for stack_line in stacks_str.split("\n")[:-1]:
    for i, let_pos in enumerate(indices_of_letters):
        if stack_line[let_pos] != " ":
            stacks[i+1].insert(0, stack_line[let_pos])
        


stacks2 = copy.deepcopy(stacks)

for line in A_input.split("\n"):
    words = line.split()
    
    for i in range(int(words[1])):
        
        to = int(words[-1])
        fr = int(words[3])
            
        stacks[to].append(stacks[fr][-1])        
        stacks[fr] = stacks[fr][:-1]


word = ''
for i in range(1,10):   
    word += stacks[i][-1]
print(word)


## %%part two

for line in A_input.split("\n"):
    words = line.split()
    
    amount = int(words[1]) 
    to = int(words[-1])
    fr = int(words[3])
        
    stacks2[to] += stacks2[fr][-amount:]  
    stacks2[fr] = stacks2[fr][:-amount]


word2 = ''
for i in range(1,10):
    word2 += stacks2[i][-1]
    
print(word2)



