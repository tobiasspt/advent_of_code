#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
import numpy as np

with open("input.txt", "r") as f:    
    A = f.read()
lines = A.split()


#%% Part 1
mytimestamp = int(lines[0])
busses = lines[1].split(',')
running_busses = [int(x) for x in busses if x != 'x']
waiting_minutes = [x - mytimestamp%x for x in running_busses]
best_bus_index = np.argmin(waiting_minutes)
solution1 = running_busses[best_bus_index] * waiting_minutes[best_bus_index]
print(f"Solution 1:\n{solution1}")



#%% Part 2

"""
Looping over one bus after the other. Find out at which timestep the condition
is fullfilled the first time. Then for the next bus, this condition is only
fulfilled at times = offset + n * previous_bus_id
"""

time_differences = [i for i in range(len(busses)) if busses[i] != "x"]
all
timestep = 1
offset = 0

for bus, deltaT in zip(running_busses[:], time_differences[:]):

    i = 0
    solution_found = False
    possible_times = []
    while True:
        i+=1 
        timestamp_proposed = float(i*timestep) + offset
        arrival_bus = timestamp_proposed + deltaT
    
        if arrival_bus%bus == 0:
            possible_times.append(timestamp_proposed)
            if len(possible_times) == 2:
                break

          
    timestep  = np.diff(possible_times)[0]
    offset = possible_times[0]

solution2 = int(offset)
print(f"Solution 2:\n{solution2}")
