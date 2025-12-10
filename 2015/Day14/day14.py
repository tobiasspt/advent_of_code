#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import numpy as np

def get_reindeers(reindeers_raw: list[str]) -> list[tuple[str, int, int, int]]:
    reindeers = []
    for reindeer in reindeers_raw:
        words = reindeer.split()
        name = words[0]
        speed = int(words[3])
        flight_duration = int(words[6])
        pause_duration = int(words[-2])
        reindeers.append((name, speed, flight_duration, pause_duration))
    return reindeers

def get_distance(reindeer: tuple[str, int, int, int], time: int) -> tuple[[int], list[int]]:
    name, speed, flight_duration, pause_duration = reindeer
    speeds = [speed]*flight_duration + [0]*pause_duration
    speeds = [0] + speeds * (time // len(speeds) +1)
    distance = np.cumsum(speeds)
    return distance[time], distance[:time+1]
    

with open("input.txt", "r") as f:    
    A = f.read()
reindeers_raw = A.split("\n")
reindeers = get_reindeers(reindeers_raw)

## part 1
distances = [get_distance(reindeer, 2503)[0] for reindeer in reindeers]
res1 = max(distances)
print("Solution 1:", res1)

## part 2
distance_sequence = [get_distance(reindeer, 2503)[1] for reindeer in reindeers]
distance_array = np.stack(distance_sequence)
total_points = np.zeros([distance_array.shape[0]])
for time in range(1, len(distance_sequence[0])):
    current_distances = distance_array[:, time]
    total_points += current_distances == max(current_distances)
res2 = int(max(total_points))
print("Solution 2:", res2)
    
    
    
    
