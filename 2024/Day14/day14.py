#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import numpy as np
import copy

def move_robot(robot: tuple[tuple[int,int], tuple[int,int]], seconds: int, size: list[int,int]) -> tuple[tuple[int,int]]:
    pos, vel = robot
    x,y = pos
    vx, vy = vel
    sx, sy = size
    nx = (x + vx*seconds) % sx
    ny = (y + vy*seconds) % sy
    return [(nx,ny), vel]

def get_safety_score(robots: list[tuple[tuple[int,int]]], size: list[int,int]) -> int:
    w_len = int(size[0]/2)
    t_len = int(size[1]/2)    
    Q1 = sum([1 for r in robots if r[0][0] < w_len and r[0][1] < t_len])
    Q2 = sum([1 for r in robots if r[0][0] > w_len and r[0][1] < t_len])
    Q3 = sum([1 for r in robots if r[0][0] < w_len and r[0][1] > t_len])
    Q4 = sum([1 for r in robots if r[0][0] > w_len and r[0][1] > t_len])
    return Q1*Q2*Q3*Q4
    
def center_of_gravity(robots: list[tuple[tuple[int,int]]]) -> tuple[tuple[int,int], int]:
    ## Ignoring the fact that there are periodic boundary conditions. 
    ## Its somehow justified if we assume that the Christmas tree will 
    ## not be situated on a boundary. 
    
    x_vals = np.array([r[0][0] for r in robots])
    y_vals = np.array([r[0][1] for r in robots])
    x_center = np.average(x_vals)
    y_center = np.average(y_vals)
    distances_to_center = np.sqrt((x_vals-x_center)**2 + (y_vals - y_center)**2)
    mean_distance = np.average(distances_to_center)
    return ((x_center, y_center), mean_distance)

    
## reding and parsing input
with open("input.txt", "r") as f:    
    A = f.read()
wide = 101
tall = 103
robots_input = A.split("\n")
robots = []
for r in robots_input:
    pos, vel = r.split()
    pos = [int(x) for x in pos.split("=")[1].split(",")]
    vel = [int(x) for x in vel.split("=")[1].split(",")]
    robots.append([pos,vel])

## Part 1
size = [wide, tall]
new_robots = [move_robot(r, 100, size) for r in robots]
res1 = get_safety_score(new_robots, size)
print("Solution 1:", res1)


## Plot function for part 2
field = []
for f in range(size[1]):
    line = ["." for i in range(size[0])]
    field.append(line)
def plot_robots(field, robots, size):
    for r in robots:
        pos = r[0]
        field[pos[1]][pos[0]] = '#'
    for line in field:
        print("".join(line))
        
  
## Part 2
min_distances = []
for s in range(12000):
    new_robots = [move_robot(r, s, size) for r in robots]
    g_center, dist = center_of_gravity(new_robots)
    min_distances.append(dist)
res2 = np.argmin(min_distances)
print("Solution 2:", res2)
### Plot for checking:
new_robots = [move_robot(r, res2, size) for r in robots]
plot_robots(copy.deepcopy(field), new_robots, size)

                           


