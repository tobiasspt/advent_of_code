# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np
import time


with open('input.txt', 'r') as f:
# with open('test.txt', 'r') as f:

    A_input = f.read().split('\n')
    
    
blueprints_dict = {}

for blueprint in A_input:
    words = blueprint.split()    
    
    bp_id = int(words[1].strip(':'))
    
    cost_ore = int(words[6])
    
    cost_clay = int(words[12])
    
    cost_obsidian_ore = int(words[18])
    cost_obsidian_clay = int(words[21])
    
    cost_geode_ore = int(words[27])
    cost_geode_obsidian = int(words[30])
    

    blueprints_dict[bp_id] = {'ore_cost':cost_ore, 'clay_cost':cost_clay, 
                              'obsidian_cost':(cost_obsidian_ore, cost_obsidian_clay),
                              'geode_cost': (cost_geode_ore, cost_geode_obsidian)}

t_max = 32 # minutes

# state = 

global counts
global max_geodes


def calculate_next_state(t_max, bp_id, mins, ro, rc, rob, rg, no, nc, nob, ng, toggle_build):
    global counts
    global max_geodes
    
    counts +=1
    
    # Some time has passed and still no obsidian robot -> abort mission 
    # This is not that much of a time-saver. 
    if rob == 0 and mins >= t_max - blueprints_dict[bp_id]['geode_cost'][1]/2 - 1:
        return 
    
    
    ###########################################################################
    # maximum additional geodes
    remaining = t_max - mins
    plus_geodes_max = ng*remaining
    # every min a new geode robot comes along
    remaining -= 1
    while remaining >0:
        plus_geodes_max += remaining
        remaining -= 1
    if ng + plus_geodes_max < max_geodes:
        return 
    ###########################################################################
    
    
    if mins == t_max:
        geodes = ng
        if geodes > max_geodes:
            max_geodes = geodes
        return
    
    max_number_ore  = no//blueprints_dict[bp_id]['ore_cost']
    max_number_clay = no//blueprints_dict[bp_id]['clay_cost']
    max_number_obsidian = min(no//blueprints_dict[bp_id]['obsidian_cost'][0],
                              nc//blueprints_dict[bp_id]['obsidian_cost'][1])
    
    max_number_geode = min(no//blueprints_dict[bp_id]['geode_cost'][0],
                           nob//blueprints_dict[bp_id]['geode_cost'][1])  
    
    
    new_no = no + ro
    new_nc = nc + rc
    new_nob = nob + rob
    new_ng = ng + rg
    
    max_ore_needed = max(blueprints_dict[bp_id]['geode_cost'][0], blueprints_dict[bp_id]['obsidian_cost'][0], blueprints_dict[bp_id]['clay_cost'] )

    
    #Assumption here that at each step max 1 new machine is produced
    if toggle_build[3] and max_number_geode:

        calculate_next_state(t_max, bp_id, mins+1,
                             ro, rc, rob, rg+1,
                             new_no - blueprints_dict[bp_id]['geode_cost'][0],
                             new_nc,
                             new_nob - blueprints_dict[bp_id]['geode_cost'][1],
                             new_ng,
                             [True, True, True, True])
        
        
    if toggle_build[2] and max_number_obsidian:
        calculate_next_state(t_max, bp_id, mins+1,
                             ro, rc, rob + 1, rg,
                             new_no - blueprints_dict[bp_id]['obsidian_cost'][0],
                             new_nc - blueprints_dict[bp_id]['obsidian_cost'][1],
                             new_nob,
                             new_ng,
                             [True, True, True, True])
    
    if toggle_build[1] and max_number_clay:
        calculate_next_state(t_max, bp_id, mins+1,
                             ro, rc + 1, rob, rg,
                             new_no - blueprints_dict[bp_id]['clay_cost'],
                             new_nc,
                             new_nob,
                             new_ng,
                             [True, True, True, True])
    # Create ore robot
    if toggle_build[0] and max_number_ore and ro < max_ore_needed:
        calculate_next_state(t_max, bp_id, mins+1,
                             ro + 1, rc, rob, rg,
                             new_no - blueprints_dict[bp_id]['ore_cost'],
                             new_nc,
                             new_nob,
                             new_ng,
                             [True, True, True, True])
    
    
    # No robot has been build
    toggle_new =  [not bool(max_number_ore), not bool(max_number_clay), not bool(max_number_obsidian), not bool(max_number_geode)]
    calculate_next_state(t_max, bp_id, mins+1,
                         ro, rc, rob, rg,
                         new_no,
                         new_nc,
                         new_nob,
                         new_ng,
                         toggle_new)
    


def max_geodes_calculator(t_max, bp_id ):
    
    global counts
    global max_geodes
    
    t0 = time.time()

    counts = 0
    max_geodes = 0

    calculate_next_state(t_max, bp_id, 0,
                         1, 0, 0, 0,
                         0, 0, 0, 0, 
                         [True, True, True, True])
    
    print('Time for BP:', bp_id, ', Max geodes:', max_geodes, ', Time:', np.round(time.time()-t0,2),'s')
    
    return max_geodes



#%% Part1

t_max1 = 24
max_geodes_list = []

for bp_id in range(1, len(A_input)+1):
    max_geodes_list.append(max_geodes_calculator(t_max1, bp_id))
    
res1 = np.sum(max_geodes_list*np.arange(1, len(A_input)+1))

print('res1', res1)

#%% Part2

t_max2 = 32
max_geodes_list2 = []

for bp_id in range(1, 4):
    max_geodes_list2.append(max_geodes_calculator(t_max2, bp_id))

res2 = max_geodes_list2[0]*max_geodes_list2[1]*max_geodes_list2[2]

print('res2', res2)


    

    
