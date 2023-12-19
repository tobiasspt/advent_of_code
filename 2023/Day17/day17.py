#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

def get_can_come_from(position, minimum_to_turn, maximum_straight):
    x, y, direc, straigth_dist_run  = position

    came_from_list = []
    
    if  1 < straigth_dist_run:
        if direc == "r":
            came_from = [x, y-1, direc, straigth_dist_run-1]
        elif direc == "l":
            came_from = [x, y+1, direc, straigth_dist_run-1]
        elif direc == "d":
            came_from = [x-1, y, direc, straigth_dist_run-1]
        elif direc == "u":
            came_from = [x+1, y, direc, straigth_dist_run-1]           
        came_from_list.append(came_from)
    
    
    elif straigth_dist_run == 1:
        for ii in range(minimum_to_turn, maximum_straight+1):
            
            if direc in ["r", "l"]:
                came_from_list.append([x-1, y, "d", ii])
                came_from_list.append([x+1, y, "u", ii])

            elif direc in ["u","d"]:
                came_from_list.append([x, y+1, "l", ii])
                came_from_list.append([x, y-1, "r", ii])
                
    came_from_list = [pos for pos in came_from_list if pos[0] >= 0 and pos[0] < xlen]
    came_from_list = [pos for pos in came_from_list if pos[1] >= 0 and pos[1] < xlen]
        
    came_from_list = [tuple(pos) for pos in came_from_list]
    return came_from_list


def prepare_all_state_dict(xlen, ylen, minimum_to_turn, maximum_straight, breakable=False):

    all_states_dict = {}
    
    for x in range(xlen):
        for y in range(ylen):
            for straigth_dist_run in range(1, maximum_straight+1):
                for direc in ["u","d","l","r"]:
                    
                    state = (x, y, direc, straigth_dist_run)
                    
                    
                    all_states_dict[state] = {}
                    can_come_from = get_can_come_from(state, minimum_to_turn, maximum_straight)
                    all_states_dict[state]["heat_loss"] = 1e6
                    all_states_dict[state]["can_come_from"] = can_come_from
                    
    
                    if x == 0 and y == 0:
                        all_states_dict[state]["heat_loss"] = 0
                        
                    #endpoints needs to be breakable
                    if breakable: 
                        if x == xlen-1 and y == ylen-1:
                            can_come_from = all_states_dict[state]["can_come_from"]
                            can_come_from = [pos for pos in can_come_from if pos[3] >= 4]

    return all_states_dict



def solve_minimum_heat_loss(xlen, ylen, minimum_to_turn, maximum_straight, breakable=False):

    all_states_dict = prepare_all_state_dict(xlen, ylen, minimum_to_turn, maximum_straight, breakable)

    has_changed = True
    counter = 0
    while has_changed:
        counter += 1
        
        has_changed = False
        
        for x in range(xlen):
            for y in range(ylen):
                for ii in range(1, maximum_straight+1):
                    for direc in ["u","d","l","r"]:
                            
                        pos = (x, y, direc, ii)
    
                        can_come_from = all_states_dict[pos]["can_come_from"]
                                           
                        for pos_from in can_come_from:
                            current_heat_loss = all_states_dict[pos]["heat_loss"]
                            
                            if array[x][y] + all_states_dict[pos_from]["heat_loss"] < current_heat_loss:
                                has_changed = True
                                all_states_dict[pos]["heat_loss"] = array[x][y] + all_states_dict[pos_from]["heat_loss"]
    
    return all_states_dict


def calculate_minimum_heat_loss(xlen, ylen, minimum_to_turn, maximum_straight, breakable=False):

    all_states_dict =solve_minimum_heat_loss(xlen, ylen, minimum_to_turn, maximum_straight, breakable)
    
    final_heat_losses = []
    for pos in all_states_dict:
        x, y, direc, straigth_dist_travveled = pos
        if x == xlen -1 and y == ylen -1:
            final_heat_losses.append(all_states_dict[pos]["heat_loss"])
            
    return min(final_heat_losses)


with open("input.txt", "r") as f:    
    A = f.read()

array = [[int(x) for x in list(line)] for line in A.split()]
xlen = len(array)
ylen = len(array[0])

    
res1 = calculate_minimum_heat_loss(xlen, ylen, 1, 3, False)
res2 = calculate_minimum_heat_loss(xlen, ylen, 4, 10, True)

print(f"Solution 1\n{res1}")
print(f"Solution 1\n{res2}")





