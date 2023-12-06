#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

with open("input.txt", "r") as f:    
    A = f.read()

lines = A.split("\n")
duration_list = [int(x) for x in lines[0].split(":")[1].split()]
distances = [int(x) for x in lines[1].split(":")[1].split()]


def calculate_distance(holding_time, duration):
    return holding_time *(duration - holding_time)
    
    
error_margins = []

for duration, record in zip(duration_list, distances):
    
    
    error_margin = 0
    
    for holding_time in range(0, duration+1):
        
        distance = calculate_distance(holding_time, duration)
        
        if distance > record:
            error_margin += 1

    error_margins.append(error_margin)
    
res1 = 1
for x in error_margins:
    res1*= x
    
print(f"Solution 1\n{res1}")
    
#%% Part 2


duration = int("".join(lines[0].split(":")[1].split()))
record = int("".join(lines[1].split(":")[1].split()))


error_margin = 0

for holding_time in range(0, duration+1):
    
    distance = calculate_distance(holding_time, duration)
    
    if distance > record:
        error_margin += 1
        
    if not holding_time % 10000000:
        print("completed:", holding_time/duration)
print(f"Solution 1\n{error_margin}")

#%% Part 2 fast

# find lower limit

def is_better(holding_time):
    distance = calculate_distance(holding_time, duration)
    if distance > record:
        return 1
    else:
        return 0 


ht1 = 0
st1 = is_better(ht1)

ht2 = int(duration/2)
st2 = is_better(ht2)

ht3 = duration
st3 = is_better(ht3)


# find lower limit
max_not = ht1
min_yes = ht2
while True: 
    if min_yes - max_not == 1:
        break
    test = int(max_not + (min_yes-max_not)/2)
    status = is_better(test)
    if status == 1:
        min_yes = test
    elif status == 0:
        max_not = test
range_start = min_yes


# find highe limit
min_not = ht3
max_yes = ht2
while True: 
    if min_not - max_yes == 1:
        break
    test = int(max_yes + (min_not-max_yes)/2)
    status = is_better(test)
    if status == 1:
        max_yes = test
    elif status == 0:
        min_not = test
range_end = min_not

solution2 = range_end - range_start    
print(f"Solution 2(fast) \n{solution2}")
