# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 08:07:13 2023

@author: spitaler.t
"""

import copy
import decimal
import functools
import math
import numpy as np

"""
My Ansatz:
Use the fact that some hailstones have the same velocity in the same direction.
Using this information, the allowed velocities of the rock in this direction can
be found. 

With this information I can than find the starting point in one coordinate, 
calculate the time it takes to hit some specific hail stone. 
With the time and the hailstone the origins in the other coordinates can be found. 

"""


@functools.cache
def divisorGenerator(n: int) -> list[int]:
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            large_divisors.append(i)
            if i*i != n:
                large_divisors.append(n / i)
    large_divisors = [int(x) for x in large_divisors]
    return sorted(large_divisors)


def get_common_elements(element_lists: list[list]) -> list:
    common_elements = element_lists[0]
    for i in range(1, len(element_lists)):
        common_elements = [x for x in common_elements if x in element_lists[i]]
    return common_elements


def possible_rockvels(v_hail: int, x1: int, x2: int) -> list[int]:
    
    difference = x2-x1  # is positive as it is sorted
    divisors = np.array(divisorGenerator(difference))
    possible_vels = difference/divisors + v_hail
    
    pv2 = v_hail - difference/divisors
    possible_vels = list(possible_vels) + pv2.tolist()
    
    return possible_vels
    

def test_rockvels(v_hail: int, x1: int, x2: int, test_velocities: list[int]) -> list[int]:
    possible_vels = [v for v in test_velocities if not (x2-x1)%(v-v_hail)]
    return possible_vels
    

def find_allowed_rock_velocity(cords: list[int], vels: list[int]) -> int:
    sort_index = np.argsort(cords)
    vels = np.array(vels)[sort_index]
    cords = np.array(cords)[sort_index]
    
    possible_rock_vels_list = []
    
    for i in range(len(vels)-1):
        v1 = vels[i]
        for j in range(i+1, len(vels)):
            v2 = vels[j]
            if v1 == v2:
                x1 = cords[i]
                x2 = cords[j]
                
                if len(possible_rock_vels_list) == 0:
                    possible_rock_vels_list = possible_rockvels(v1, x1, x2)
                
                elif len(possible_rock_vels_list) == 1:
                    
                    return possible_rock_vels_list[0]
                
                else:
                    possible_rock_vels_list = test_rockvels(v1, x1, x2, possible_rock_vels_list)
                    

#%% Part 1

with open("input.txt") as f:
    A = f.read()
    
posmin = 200000000000000.0
posmax = 400000000000000.0


hails_list = A.split("\n")
hail_dict = {}

for i, hail in enumerate(hails_list):
    pos, vel = hail.split("@")
    pos = [decimal.Decimal(x) for x in pos.split(",")]
    vel = [decimal.Decimal(x) for x in vel.split(",")]
    hail_dict[i] ={"pos":pos, "vel":vel}
    
valid = 0
tol = 0.1

for i in range(len(hail_dict)-1):
    for j in range(i+1, len(hail_dict)):
        
        h1 = hail_dict[i]
        h2 = hail_dict[j]
    
        x1, y1, _ = h1["pos"]
        vx1, vy1, _ = h1["vel"]
    
        x2, y2, _ = h2["pos"]
        vx2, vy2, _ = h2["vel"]
        
        if abs(vy1/vy2 - vx1/vx2) < 1e-15:
            # The hail stones are parallel
            continue
        
        t1  = ((y1-y2)  - (x1-x2)*vy2/vx2) *   (vy2*vx1/vx2 - vy1)**(-1)
        t2  = ((x1-x2) + t1*vx1)/vx2
    
        assert abs(x1 + vx1*t1 - (x2 + vx2*t2)) < tol, abs(x1 + vx1*t1 - (x2 + vx2*t2)) 
        assert abs(y1 + vy1*t1 - (y2 + vy2*t2)) < tol, abs(y1 + vy1*t1 - (y2 + vy2*t2))
    
        if t1 >= 0 and t2 >= 0:
            pd1 = float(t1)
            pd2 = float(t2)
            
            x_cross = x1 + vx1 * t1
            y_cross = y1 + vy1 * t1
    
            if posmin <= x_cross <= posmax and posmin <= y_cross <= posmax:
                valid += 1
            
print(f"Solution 1\n{valid}")
    
      
    
#%% Part 2
    
    
hail_stones = dict()

for i, line in enumerate(A.split("\n")):
    
    pos, vel = line.split("@")
    pos = np.array([float(x) for x in pos.split(",")])
    vel = np.array([float(x) for x in vel.split(",")])
    
    hail_stones[i] = {"pos": pos, "vel": vel}
    

xcords = [hail_stones[i]["pos"][0] for i in range(len(hail_stones))]
ycords = [hail_stones[i]["pos"][1] for i in range(len(hail_stones))]
zcords = [hail_stones[i]["pos"][2] for i in range(len(hail_stones))]

xvels = [hail_stones[i]["vel"][0] for i in range(len(hail_stones))]
yvels = [hail_stones[i]["vel"][1] for i in range(len(hail_stones))]
zvels = [hail_stones[i]["vel"][2] for i in range(len(hail_stones))]


allowed_rock_velocites = []

for cords, vels in zip([xcords, ycords, zcords], [xvels, yvels, zvels]):
    allowed_rockvel = find_allowed_rock_velocity(cords, vels)
    allowed_rock_velocites.append(int(allowed_rockvel))



# I choose the x-coordinates for finding the start point of the rock
    
sort_index = np.argsort(xcords)
vels = np.array(xvels)[sort_index]
cords = np.array(xcords)[sort_index]
    
vels = [int(x) for x in vels]
cords = [int(x) for x in cords]

vrock = allowed_rock_velocites[0]


starters = []
for i in range(len(vels)):
    v1 = vels[i]
    x1 = cords[i]
    start1 = x1 + (v1-vrock)
    d1 = v1 - vrock
    starters.append((start1, d1))
    

def find_common_x0(start1, start2, delta1, delta2):
    assert delta1 != 0
    assert delta2 != 0
    
    # If the current start point (start1) fits also for the second hail, 
    # the start point is accepted. 
    if not (start1-start2)%abs(delta2):
        return (start1, delta1)
    
    new_range = []
    if start2 > start1:
        counter = np.floor((start2-start1)/abs(delta1))-1
    else:
        counter = -1
    
    while len(new_range) < 3:
        guess = start1 + counter*delta1
        counter += 1
        
        test = (guess-start2)%delta2
        
        if not test:
            new_range.append(guess)
    
    _diffs = np.diff(new_range)
    assert _diffs[0] == _diffs[1]
            
    return (int(new_range[0]), int(_diffs[0]))



# Finding the x0
all_ranges = copy.deepcopy(starters)
current_r = all_ranges.pop(0)

while len(all_ranges) > 0:

    hmmpf = all_ranges.pop(0)    
    start1 = current_r[0]
    start2 = hmmpf[0]
    
    delta1 = current_r[1]
    delta2 = hmmpf[1]
    current_r = find_common_x0(start1, start2, delta1, delta2)
    
        

# Calculating the time from the foudn x0 and then calculating the other coordinates
x0 = current_r[0]
x0hail = xcords[0]
vhail = xvels[0]

t = (x0 -x0hail) / (vhail - vrock)
xspeed, yspeed, zspeed = allowed_rock_velocites
y0 = ycords[0] + yvels[0]*t - yspeed*t
z0 = zcords[0] + zvels[0]*t - zspeed*t

print(f"Solution 2\n{int(x0+y0+z0)}")



