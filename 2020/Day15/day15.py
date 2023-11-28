#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
from collections import defaultdict
import numpy as np

with open("input.txt", "r") as f:    
    A = f.read()
numbers = np.array(A.split(','), dtype=int)


def xth_number_spoken(x):
    number_dict = defaultdict(lambda: {"last_appearance":0, "appearances":0, "age":None})
    
    #Initializing the game
    timestep = 0 
    for number in numbers:
        timestep += 1
        
        number_dict[number]["last_appearance"] = timestep
        number_dict[number]["appearances"] +=1
        

    for i in range(x - len(numbers)):
        timestep += 1 
       
        if number_dict[number]["appearances"] == 1:
            number = 0
        else:
            number = number_dict[number]["age"]
        number_dict[number]["age"] = timestep - number_dict[number]["last_appearance"]
        number_dict[number]["last_appearance"] = timestep
        number_dict[number]["appearances"] +=1
    return number


#%% Part 1
solution1 = xth_number_spoken(2020)
print(f"Solution 1:\n{solution1}")
 
#%% Part 2
solution2 = xth_number_spoken(30000000)
print(f"Solution 1:\n{solution2}")


