# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""

import hashlib as hs

def get_hexagonal_MD5_hash(string: str) -> str:
    return hs.md5(string.encode()).hexdigest()


def get_4_chars_of_hash(string: str) -> str:
    return get_hexagonal_MD5_hash(string)[:4]


def is_open(char: str) -> bool:
    if char in ["b", "c", "d", "e", "f"]:
        return True
    else:
        return False
    
    
"""
4x4 grid. 
x goes from 0 to 3 (west to east)
y goes from 0 to 3 (north to south)
start is at 0,0
"""

def get_next_positions(pos: tuple[int, int], path: str) -> list[tuple[int,int], str]:
    """
    4x4 grid. 
    x goes from 0 to 3 (west to east)
    y goes from 0 to 3 (north to south)
    start is at 0,0
    """
    
    if pos == (3,3):
        return path
    x,y = pos
    
    pos_hash = get_4_chars_of_hash(path)
    
    door_status_list = [is_open(char) for char in pos_hash]
    directions_list = ["U", "D", "L", "R"]
    new_positions = [(x-1,y), (x+1,y), (x,y-1), (x, y+1)]

    new_positions_to_check = []
    for new_pos, door_status, direction in zip(new_positions, door_status_list, directions_list):
        if not door_status:
            continue
        x,y = new_pos
        if x<0 or x>3 or y<0 or y>3:
            continue
        
        new_positions_to_check.append((new_pos, path+direction))
        
    return new_positions_to_check


#%% part 1

#Reading the input
with open('input.txt','r') as f:    
    A = f.read()
initial_path = A


current_positions = [((0,0), initial_path)]

result1 = None
while True:
    
    new_positions = []
    
    for pos, path in current_positions:
        np = get_next_positions(pos, path)
        if type(np) == str:
            result1 = np
        else:
            new_positions += np
        
    if result1 is not None:
        break
        
    current_positions = new_positions
    if len(current_positions) == 0:
        print("Cannot reach the end!")
        break
    
solution1 = result1[len(initial_path):]
print("Soluton 1:", solution1)
    

#%% part 2


initial_path = A

current_positions = [((0,0), initial_path)]

paths_to_target = []
while True:
    new_positions = []
    
    for pos, path in current_positions:
        np = get_next_positions(pos, path)
        if type(np) == str:
            paths_to_target.append(np)
        else:
            new_positions += np

    current_positions = new_positions
    if len(current_positions) == 0:
        # print("No more paths to check!")
        break
    
solution2 = max([len(x) for x in paths_to_target]) - len(initial_path)
print("Soluton 2:", solution2)
        



  

#%%


