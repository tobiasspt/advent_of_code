# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""

from functools import lru_cache
from collections import defaultdict

#Reading the input
with open('input.txt','r') as f:    
    A = f.read()
    
designers_favourite_number = int(A)
target = (31, 39)

   
def equation(x: int, y:int) -> int:
    return x*x + 3*x + 2*x*y + y + y*y

def location_code(x: int, y:int) -> int:
    return   equation(x, y) + designers_favourite_number
    
@lru_cache()
def is_open_space(pos: tuple[int,int]) -> bool:
    x, y = pos
    
    #only positivie integers
    if x < 0:
        return False
    if y < 0:
        return False
    
    number = location_code(x, y)
    binary = bin(number)[2:]
    number_of_1 = binary.count("1")
    
    if number_of_1%2 == 0:
        return True
    else:
        return False
    




memory = defaultdict(lambda: 1000)
number_of_steps_needed = []
def go_to_next_place(position: tuple[int, int], steps: int) -> None:
    
    if position == target:
        number_of_steps_needed.append(steps)
        print("Number of steps needed:", steps)
        return 
        
    if steps >= memory[position]:
        return
    else:
        memory[position] = steps
    
    x,y = position
    for next_pos in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if is_open_space(next_pos):
            go_to_next_place(next_pos, steps+1)

position = (1,1)
steps = 0
go_to_next_place(position, steps)
print("Solution 1", min(number_of_steps_needed))
    


#%% Part 2


possible_positions = []
memory = defaultdict(lambda: 1000)
def discover_the_area(position: tuple[int, int], steps: int) -> None:

    max_steps = 50
    if steps > max_steps:
        return
    else:
        possible_positions.append(position)
    
    if steps >= memory[position]:
        return
    else:
        memory[position] = steps
    
    x,y = position
    for next_pos in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if is_open_space(next_pos):     
            discover_the_area(next_pos, steps+1)
    
discover_the_area((1,1), 0)
    
solution2 = len(set(possible_positions))
print("Solution 2", solution2)