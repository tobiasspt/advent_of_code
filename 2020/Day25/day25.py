#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

with open("input.txt", "r") as f:    
    A = f.read()

card_public_key, door_public_key = [int(x) for x in A.split()]

def transform_subject_number(subject_number, loop_size, value=1):     
    for i in range(loop_size):
        value *= subject_number
        value = value%20201227  
    return value
        
        
def calculate_loop_size(key):
    value = 1
    loop_size = 1
    while True:
        value = transform_subject_number(7, 1, value)
        if value == key:
            break
        else:
            loop_size += 1
    return loop_size

card_loop_size = calculate_loop_size(card_public_key)
door_loop_size = calculate_loop_size(door_public_key)


encryption_key = transform_subject_number(door_public_key, card_loop_size)
# encryption_key1= transform_subject_number(card_public_key, door_loop_size)
print(f"Solution:\n{encryption_key}")


