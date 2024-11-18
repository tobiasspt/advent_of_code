# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""
import numpy as np

#Reading the input
with open('input.txt','r') as f:    
    A = f.read()

# A = """ULL
# RRDDD
# LURDL
# UUUUD"""

instruction_list = A.split("\n")

# 1 2 3
# 4 5 6
# 7 8 9 

def make_step(step, posx, posy):
    if step == "U" and  posy > -1: 
        posy -= 1
    elif step == "D" and posy < 1:
        posy += 1
    elif step == "L" and posx > -1:
        posx -= 1
    elif step == "R" and posx < 1:
        posx += 1
    
    return posx, posy
        
def number(posx, posy):
    
    if posx == -1:
        if posy == -1:
            return 1
        elif posy == 0:
            return 4
        elif posy == 1:
            return 7
    elif posx == 0:
        if posy == -1:
            return 2
        elif posy == 0:
            return 5
        elif posy == 1:
            return 8
    elif posx == 1:
       if posy == -1:
           return 3
       elif posy == 0:
           return 6
       elif posy == 1:
           return 9

def decode_instructions(instruction, posx, posy):
    
    steps = instruction[:]
    for step in steps:
        posx, posy = make_step(step, posx, posy)
    return posx, posy

posx = 0
posy = 0
solution1 = 0
for instruction, exponent in zip(instruction_list, np.arange(len(instruction_list))[::-1]):
    posx, posy = decode_instructions(instruction, posx, posy)
    solution1 += number(posx, posy)*10**exponent
    
print("Solution 1:", solution1)
#3662 is too low

#%% part 2

way_dict = {1: {"U": 1, "D": 3, "L":1, "R": 1},
            2: {"U": 2, "D": 6, "L":2, "R": 3}, 
            3: {"U": 1, "D": 7, "L":2, "R": 4},
            4: {"U": 4, "D": 8, "L":3, "R": 4},
            5: {"U": 5, "D": 5, "L":5, "R": 6},
            6: {"U": 2, "D": "A", "L":5, "R": 7},
            7: {"U": 3, "D": "B", "L":6, "R": 8},
            8: {"U": 4, "D": "C", "L":7, "R": 9},
            9: {"U": 9, "D": 9, "L":8, "R": 9},
            "A": {"U": 6, "D": "A", "L":"A", "R": "B"},
            "B": {"U": 7, "D": "D", "L":"A", "R": "C"},
            "C": {"U": 8, "D": "C", "L":"B", "R": "C"},
            "D": {"U": "B", "D": "D", "L":"D", "R": "D"},
            }
    
def find_next_number(instruction, position):
    for step in instruction[:]:
        position = way_dict[position][step]
    return position

position = 5
solution2 = str()
for instruction, exponent in zip(instruction_list, np.arange(len(instruction_list))[::-1]):
    position = find_next_number(instruction, position)
    solution2 += str(position)

print("Solution 2:", solution2)
        
   


