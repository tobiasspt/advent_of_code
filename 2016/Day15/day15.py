# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""


def first_time_at_slot(disc_number: int, disc: dict) -> int:
    
    start_time = -1
    while True:
        start_time += 1
        time_to_disc = start_time + disc_number
        
        disc_pos = disc["start_pos"] + time_to_disc
        disc_pos = disc_pos % disc["count_pos"]
        if disc_pos == 0:
            return start_time
            

def add_disc(disc_dict: dict, d_number: int, start_position: int, count_position: int) ->None:
    
    disc_dict[d_number] = {"start_pos": start_position, "count_pos": count_position }
    first_slot_time = first_time_at_slot(d_number, disc_dict[d_number])
    disc_dict[d_number]["first_slot_time"] = first_slot_time



def find_common_start_time_and_timestep(start_t_1: int, t_step_1: int, start_t_2: int, t_step_2: int) -> tuple[int, int]:
    
    try_time = start_t_1
    okay_times = []
    
    while len(okay_times) < 2:
        test = try_time - start_t_2
        if test > 0 and test%t_step_2 == 0:
            okay_times.append(try_time)
        try_time += t_step_1
            
    new_start_t = okay_times[0]
    new_t_step = okay_times[1] - okay_times[0]
    
    return new_start_t, new_t_step
        


def find_common_start_time_from_many(processes: list[tuple[int,int]]) -> int:
    
    process_0 = processes[0]
    start_time, time_step = process_0
    
    for process_1 in processes[1:]:
        d_st, d_ss = process_1
        start_time, time_step = find_common_start_time_and_timestep(start_time, time_step, d_st, d_ss)
        
    return start_time
    

#%% part 1
#Reading the input
with open('input.txt','r') as f:    
    A = f.read()
discs_input = A.split("\n")

disc_dict = {}
for i, disc in enumerate(discs_input):
    
    words = disc.split()
    count_position = int(words[3])
    start_position = int(words[-1][:-1])
    
    add_disc(disc_dict, i+1, start_position, count_position)
    
processes = [(disc["first_slot_time"], disc["count_pos"]) for disc in disc_dict.values()]

solution1 = find_common_start_time_from_many(processes)
print("Solution 1", solution1)
    
    
#%% Part 2
add_disc(disc_dict, len(discs_input)+1, 0, 11)
processes = [(disc["first_slot_time"], disc["count_pos"]) for disc in disc_dict.values()]
solution2 = find_common_start_time_from_many(processes)
print("Solution 2", solution2)

