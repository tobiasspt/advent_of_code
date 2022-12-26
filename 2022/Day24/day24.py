# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

"""
x -> +
y 
|
v
+

pos = (y, x)
"""

with open('input.txt', 'r') as f:
# with open('test.txt', 'r') as f:
    A_input = f.read().split('\n')


leny = len(A_input)
lenx = len(A_input[0])

walls = set()
left = set()
right = set()
down = set()
up = set()


for yindex, line in enumerate(A_input):
    
    line_array = np.array(list(line), dtype=str)    
    
    w_new = {(yindex, x) for x in np.where(line_array=='#')[0]}
    walls = walls.union(w_new)
    
    l_new = {(yindex, x) for x in np.where(line_array=='<')[0]}
    left = left.union(l_new) 

    r_new = {(yindex, x) for x in np.where(line_array=='>')[0]}
    right = right.union(r_new) 

    u_new = {(yindex, x) for x in np.where(line_array=='^')[0]}
    up = up.union(u_new) 

    d_new = {(yindex, x) for x in np.where(line_array=='v')[0]}
    down = down.union(d_new) 

walls.add((-1,1))
walls.add((leny, lenx-2))

def draw_grove(walls, left, right, down, up, me):
    ms = 3 #markersize
    
    fig = plt.figure(dpi=200, figsize=[10,3])
    ax = fig.gca()
    ax.plot([w[1] for w in walls], [w[0] for w in walls],'kx', markersize=ms)
    
    ax.plot([w[1] for w in up], [w[0] for w in up],'k^', markersize=ms, label='up')
    ax.plot([w[1] for w in down], [w[0] for w in down],'kv', markersize=ms, label='up')
    ax.plot([w[1] for w in left], [w[0] for w in left],'k<', markersize=ms, label='up')
    ax.plot([w[1] for w in right], [w[0] for w in right],'k>', markersize=ms, label='up')

    ax.invert_yaxis()

start = (0,1)
draw_grove(walls, left, right, down, up, start)

# We can make a table of the blizzards, as the same configurations will appear 
# after lenx*leny mins

rotation_x = lenx - 2
rotation_y = leny - 2

blizzard_dict = {}

def wrap_back_x(x):
    
    if x%rotation_x == 0:
        return rotation_x
    elif x < 0:
        return x%rotation_x
    elif x > rotation_x:
        return x%rotation_x
    else:
        return x

def wrap_back_y(y):
    
    if y%rotation_y == 0:
        return rotation_y
    elif y < 0:
        return y%rotation_y
    elif y > rotation_y:
        return y%rotation_y
    else:
        return y 


for i in range(rotation_x*rotation_y):
    
    blizzard_dict[i] = {}

    new_left = {(x[0], wrap_back_x(x[1]-i)) for x in left}
    blizzard_dict[i]['left'] = new_left
    
    new_right = {(x[0], wrap_back_x(x[1]+i)) for x in right}
    blizzard_dict[i]['right'] = new_right
    
    new_up = {(wrap_back_y(x[0]-i), x[1]) for x in up}
    blizzard_dict[i]['up'] = new_up
    
    new_down = {(wrap_back_y(x[0]+i), x[1]) for x in down}
    blizzard_dict[i]['down'] = new_down
    
    blizzard_dict[i]['walls'] = walls
    blizzard_dict[i]['me'] = (0,1)
    
    blizzard_dict[i]['blocked'] = new_left.union(new_right).union(new_up).union(new_down).union(walls)
    
    
pos_dict = defaultdict(lambda: defaultdict(lambda: True))

for timestep in blizzard_dict.keys():
    
    for w in walls:
        pos_dict[w][timestep] = False
    for x in blizzard_dict[timestep]['right']:
        pos_dict[x][timestep] = False
    for x in blizzard_dict[timestep]['left']:
        pos_dict[x][timestep] = False
    for x in blizzard_dict[timestep]['up']:
        pos_dict[x][timestep] = False
    for x in blizzard_dict[timestep]['down']:
        pos_dict[x][timestep] = False


def manhatten(p1,p2):
    return np.abs(p1[0]-p2[0]) + np.abs(p1[1]-p2[1])




    
#%%


def move_to(start_time, start, goal, reverse=False):
    
    #status_tuple  mins posy, posx, curent dist, min_dist_to_target_reached
    status_list = [(start_time, start[0], start[1], manhatten(start, goal), manhatten(start, goal))]

    set_of_explored = set()

    fewest_mins = 3000+start_time


    while len(status_list) > 0:
        
        status = status_list[-1]
            
        if status in set_of_explored:
            del status_list[-1]
            continue
        else:
            set_of_explored.add(status)
        
        
        mins = status[0]
        pos = (status[1], status[2])
        current_dist = status[3]
        min_dist_to_target = status[4]
        
    
        #reached the goal
        if pos == goal:
            proposed = mins
            # print('Finished', pos, proposed)
            if proposed < fewest_mins:
                fewest_mins = proposed
            del status_list[-1]
            continue
           
        # can no longer be faster
        if mins + 1 + current_dist > fewest_mins:
            del status_list[-1]
            continue
            
        # going other direction than towards the goal.
        if current_dist > min_dist_to_target + 3:
            del status_list[-1]
            continue
        
        new_status = []
    
        new_posis = [(pos[0]-1, pos[1]), (pos[0], pos[1]-1), pos, (pos[0]+1, pos[1]), (pos[0], pos[1]+1)]
        new_distance_to_target = [1,1,0,-1,-1]
    
        if reverse:
            new_posis = new_posis[-1::-1]
    
        for new_pos, dd in zip(new_posis, new_distance_to_target):
            if pos_dict[new_pos][(mins+1)%(rotation_x*rotation_y)]:
                new_status.append((mins+1, new_pos[0], new_pos[1], current_dist+dd, min(min_dist_to_target, current_dist+dd)))
    
        del status_list[-1]
        status_list += new_status
    
    print('Goal reached in', fewest_mins)
    return fewest_mins
    
start = (0,1)
goal = (rotation_y+1, rotation_x)
sol1 = move_to(0, (0,1), goal)

time_back = move_to(sol1, goal, start, reverse=True)

sol2 = move_to(time_back, start, goal)

print('Solution 1:', sol1)
print('Solution 2:', sol2)

