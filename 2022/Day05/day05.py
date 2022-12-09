# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np
import copy


"""
        [H]     [W] [B]            
    [D] [B]     [L] [G] [N]        
[P] [J] [T]     [M] [R] [D]        
[V] [F] [V]     [F] [Z] [B]     [C]
[Z] [V] [S]     [G] [H] [C] [Q] [R]
[W] [W] [L] [J] [B] [V] [P] [B] [Z]
[D] [S] [M] [S] [Z] [W] [J] [T] [G]
[T] [L] [Z] [R] [C] [Q] [V] [P] [H]
 1   2   3   4   5   6   7   8   9 """

stacks = {}

stacks[1] = ['T','D','W','Z','V','P']
stacks[2] = ['L','S','W','V','F','J','D']
stacks[3] = ['Z','M','L','S','V','T','B','H']
stacks[4] = ['R','S','J']
stacks[5] = ['C','Z','B','G','F','M','L','W']
stacks[6] = ['Q','W','V','H','Z','R','G','B']
stacks[7] = ['V','J','P','C','B','D','N']
stacks[8] = ['P','T','B','Q']
stacks[9] = ['H','G','Z','R','C']


stacks2 = copy.deepcopy(stacks)


with open('input.txt', 'r') as f:
    A_input = f.read().split('\n')


for line in A_input:
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

for line in A_input:
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



