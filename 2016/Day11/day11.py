# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""

from collections import defaultdict



def is_status_valid(status: dict[int, dict]) -> bool:
    
    for floor in status.keys():        
        ## danger only, if there is a generator at this floor
        if len(status[floor]["gen"]) > 0:
            for mc in status[floor]["mc"]:
                if not mc in status[floor]["gen"]:
                    return False
    ## all floors checked. It is save
    return True



def is_finished(status: dict[int, dict]) -> bool:
    
    condition_1 = len(status[1]["gen"]) == 0  and len(status[2]["gen"]) == 0  and len(status[3]["gen"]) == 0
    condition_2 = len(status[1]["mc"]) == 0  and len(status[2]["mc"]) == 0  and len(status[3]["mc"]) == 0
    
    if condition_1 and condition_2:
        return True
    else:
        return False
    


def normalize_state(status: dict[int, dict], current_floor: int, symbols: list[str]) -> [list[int,int], str]:
    """
    Normalizes the state and returns the pairs and a hash. 
    We take use of the fact, that the different elements can be interchanged. 
    """
    pairs = []
    for sym in symbols:
        
        for floor in [1,2,3,4]:
            if sym in status[floor]["gen"]:
                xgen = floor
            if sym in status[floor]["mc"]:
                xmc = floor
                
        pairs.append([xgen, xmc])
        pairs = sorted(pairs, key = lambda x : (x[0], x[1]))
    
    state_hash = str(current_floor)+'_'+str(pairs)
    return pairs, state_hash




def update_status(status: dict[int, dict], mc_moved: list[int], gen_moved: list[int],
                  floor: int, steps: int, symbols: list[str]) -> None:
    
    neighbours_dict = {}
    neighbours_dict[1] = [2]
    neighbours_dict[2] = [3,1]
    neighbours_dict[3] = [4,2]
    neighbours_dict[4] = [3]

    for new_floor_number in neighbours_dict[floor]:
        
        new_status = {}
        for _floor in [1,2,3,4]:
            new_status[_floor] = {}
            for _item in ["gen", "mc"]:
                new_status[_floor][_item] = [item for item in status[_floor][_item]]
        
        for mc in mc_moved:
            new_status[floor]["mc"].remove(mc)
            new_status[new_floor_number]["mc"].append(mc)
        for gen in gen_moved:
            new_status[floor]["gen"].remove(gen)
            new_status[new_floor_number]["gen"].append(gen)

        # print(new_status)
        evaluate_status(new_status, new_floor_number, steps+1, symbols)
        
        
        
minimum_steps = 100
number_of_steps_needed = []    

status_cache = defaultdict(lambda: minimum_steps)   

def evaluate_status(status: dict[int, dict], floor: int, steps: int, symbols: list[str]) -> None: 
    global minimum_steps
    
    print(minimum_steps, steps)
    
    ##Check if the current status is valid or slower than previous ones
    if steps >= minimum_steps:
        return
    
    if not is_status_valid(status):
        return 
    
    if is_finished(status):
        print("Finished wiht", steps, "steps")
        number_of_steps_needed.append(steps)
        if steps < minimum_steps:
            minimum_steps = steps
        return 
    
    _pairs, status_hash = normalize_state(status, floor, symbols)
    if steps >= status_cache[status_hash]:
        return
    else:
        status_cache[status_hash] = steps
        
        
        
    # """
    # Possible moves: 
    #     move 1 microchip
    #     move 2 microchips
    #     move 1 generator
    #     move 2 generators
    #     move the compatible microchip and generator
    # """
    

    ## move one mc or the mc and its generators
    for mc in status[floor]["mc"]:
        mc_moved = [mc]
        gen_moved = []
        update_status(status, mc_moved, gen_moved, floor, steps, symbols)
        
        if mc in status[floor]["gen"]:
            mc_moved = [mc]
            gen_moved = [mc]
            update_status(status, mc_moved, gen_moved, floor, steps, symbols)

    # moove two mc
    mc_number = len(status[floor]["mc"])
    if mc_number >= 2:
        for i in range(mc_number-1):
            for j in range(i+1, mc_number):
                mc_moved = [status[floor]["mc"][i], status[floor]["mc"][j]]
                gen_moved = []
                update_status(status, mc_moved, gen_moved, floor, steps, symbols)
                
    ## moove one generator
    for gen in status[floor]["gen"]:
        mc_moved = []
        gen_moved = [gen]
        update_status(status, mc_moved, gen_moved, floor, steps, symbols)

    ## move two generators
    gen_number = len(status[floor]["gen"])
    if gen_number >= 2:
        for i in range(gen_number-1):
            for j in range(i+1, gen_number):
                mc_moved = []
                gen_moved = [status[floor]["gen"][i], status[floor]["gen"][j]]
                update_status(status, mc_moved, gen_moved, floor, steps, symbols)





#%%

#Reading the input
with open('input.txt','r') as f:    
    A = f.read()




# Part 1

status = dict()
symbols = []

for i, floor in enumerate(A.split("\n")):
    floor_number = i + 1
    objects = floor.split(" a ")[1:]

    generators = []
    microchips = []
    
    for obj in objects:
        if "generator" in obj:
            generators.append(obj[:2])
            symbols.append(obj[:2])
        elif "microchip" in obj:
            microchips.append(obj[:2])
            
    status[floor_number] = {"gen":generators, "mc": microchips}
    

evaluate_status(status, 1, 0, symbols)
print("Solution 1:", min(number_of_steps_needed))


#%% 

### Part 2
status = dict()
symbols = []

for i, floor in enumerate(A.split("\n")):
    floor_number = i + 1
    objects = floor.split(" a ")[1:]

    generators = []
    microchips = []
    
    for obj in objects:
        if "generator" in obj:
            generators.append(obj[:2])
            symbols.append(obj[:2])

        elif "microchip" in obj:
            microchips.append(obj[:2])
            
    status[floor_number] = {"gen":generators, "mc": microchips}
    
status[1]["gen"] += ["el", "di"]
symbols += ["el", "di"]
status[1]["mc"] += ["el", "di"]


evaluate_status(status, 1, 0, symbols)
print("Solution 1:", min(number_of_steps_needed))


    