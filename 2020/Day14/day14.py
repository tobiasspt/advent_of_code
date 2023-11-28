#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: tobias
"""

import numpy as np


with open("input.txt", "r") as f:    
    A = f.read()
lines = A.split('\n')


def dec_to_bin(dec, num_bits=36):
    "Returns 36 bit binary"
    bina = list(bin(dec)[2:])
    binary = ["0"]*num_bits
    binary[num_bits-len(bina):] = bina
    return binary

def apply_mask(binary, mask):
    for i, m in zip(range(36), mask):
        if m != "X":
            binary[i] = m
    return binary

def binary_to_dec(binary):
    "returns a decimal from a binary, where the bits are stored in a list"
    return int("".join(binary),2)


#%% Part 1
memory_dict = {}

for line in lines:
    words = line.split()
    if words[0] == 'mask':
        mask = list(words[-1])
    else:
        memory_adress = words[0].split('[')[-1][:-1]
        memory_dict[memory_adress] = apply_mask(dec_to_bin(int(words[-1])), mask)
total_sum = sum([binary_to_dec(x) for x in memory_dict.values()])

print(f"Solution 1:\n{total_sum}")

#%% Part 2

def apply_mask_to_mem(binary, mask):
    for i, m in zip(range(36), mask):
        if m == "1":
            binary[i] = "1"
    return binary


def get_all_memory_adresses(memory_adress, mask):
    
    adress_bin = dec_to_bin(memory_adress)
    adress_bin = apply_mask_to_mem(adress_bin, mask)
    floating = np.where(np.array(mask)=="X")[0]
    n_adresses = 2**len(floating)

    possible_adresses = []
    for i in range(n_adresses):
        floating_bin = dec_to_bin(i, num_bits=len(floating))

        new_adress = np.array(adress_bin)
        new_adress[floating] = floating_bin
        possible_adresses.append(new_adress)
    return possible_adresses
    
   
memory_dict_2 = {}
for line in lines:
    words = line.split()
    if words[0] == 'mask':
        mask = list(words[-1])
    else:
        value = dec_to_bin(int(words[-1]))
        memory_adress = int(words[0].split('[')[-1][:-1])
        possible_adresses = get_all_memory_adresses(memory_adress, mask)
        for adress in possible_adresses:
            memory_dict_2["".join(adress)] = value
        
 
total_sum_2 = sum([binary_to_dec(x) for x in memory_dict_2.values()])
print(f"Solution 2:\n{total_sum_2}")
