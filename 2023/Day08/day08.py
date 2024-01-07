#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: tobias
"""


with open("input.txt", "r") as f:    
    A = f.read()

instructions = A.split("\n\n")[0]
nodes_input = A.split("\n\n")[1].split("\n")
nodes_dict = {}
for node in nodes_input:
    name, destinations = node.split(" = ")
    destinations = destinations[1:-1].split(", ")
    nodes_dict[name] = destinations

instructions = [0 if x =="L" else 1 for x in list(instructions)]
num_instructions = len(instructions)

steps = 0
position = "AAA"

while position != "ZZZ":
    inst = instructions[steps%num_instructions]
    position = nodes_dict[position][inst]
    steps += 1

print(f"Solution 1\n{steps}")


#%% Part 2



"""
A short examination shows, that each start node always ends up in the same end node.
A further examination shows, that the occurance of ending at an "end tile" is periodic
with allways the same time-difference. 
"""

start_dict_A = {}

for pos in nodes_dict.keys():
    if pos[-1] == "A":
        start = pos
        steps = 0
        z_pooints_times = []
        
        while True:
            inst = instructions[steps%num_instructions]
            pos = nodes_dict[pos][inst]
            if pos[-1] == "Z":
                z_pooints_times.append(steps+1)
                
            if len(z_pooints_times) == 2:
                break
                
            steps += 1

        start_dict_A[start] = z_pooints_times
    



keys = list(start_dict_A.keys())


def find_common_times(times1: int, times2: int) -> list[int, int]:
    
    delta1 = times1[1] - times1[0]
    delta2 = times2[1] - times2[0]    
        
    if delta1 >= delta2:
        start = times1[0]
        delta = delta1
        checkstart = times2[0]
        checkdelta = delta2
        
    elif delta2 > delta1:
        start = times2[0]
        delta = delta2
        checkstart = times1[0]
        checkdelta = delta1
        
    else: # The ranges have the same time step
        return 
    
    new_range = []
    counter = 0
    while len(new_range) < 2:
        guess = start + counter*delta
        counter += 1
        if not (guess-checkstart)%checkdelta:
            new_range.append(guess)
        
    return new_range

        
new_range = start_dict_A[keys[0]]
for key in keys[1:]:
    new_range = find_common_times(new_range, start_dict_A[key])

print(f"Solution 2\n{min(new_range)}")