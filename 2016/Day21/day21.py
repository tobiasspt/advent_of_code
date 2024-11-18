# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""

import numpy as np
from itertools import permutations


def swap_pos_x_wiht_y(string: list[str], x: int, y: int) -> list[str]:
    
    char_x = string[x]
    char_y = string[y]
    string[x] = char_y
    string[y] = char_x
    return string
    

def swap_letter_x_with_y(string: list[str], x: str, y: str) -> list[str]:
    
    ind_x = string.index(x)
    ind_y = string.index(y)
    return swap_pos_x_wiht_y(string, ind_x, ind_y)


def rotate_X_steps(string: list[str], X: int, is_left: bool) -> list[str]:
    
    new_indices = np.arange(len(string))
    if is_left:
        new_indices += X
    else:
        new_indices -= X
    new_indices = new_indices%len(string)
    new_string = [string[ind] for ind in new_indices]
    return new_string
    
    
def rotate_based_on_pos(string: str, letter: str) -> list[str]:
    
    index_start = string.index(letter)
    num_rotations = 1
    if index_start >= 4:
        num_rotations += 1
    num_rotations += index_start
    new_string = rotate_X_steps(string, num_rotations, False)
    return new_string
    

def reverse_pos_x_through_y(string: list[str], x: int, y: int) -> list[str]:
    
    new_string = string[:x]
    new_string += string[x:y+1][::-1]    
    new_string += string[y+1:]
    assert len(new_string) == len(string)
    return new_string


def move_pos_X_to_Y(string: list[str], x: int, y: int) -> list[str]:
    to_move = string[x]
    del string[x]
    string.insert(y, to_move)
    return string
    

def decifer_instruction(string: list[str], instruction: str) -> list[str]:
    
    words = instruction.split()
    if "swap position" in instruction:
        new_string = swap_pos_x_wiht_y(string, int(words[2]), int(words[5]))
    elif "swap letter" in instruction:
        new_string = swap_letter_x_with_y(string, words[2], words[5])
    elif "rotate" in words and "step" in instruction:
        if "left" in words:
            is_left = True
        else:
            is_left = False
        new_string = rotate_X_steps(string, int(words[2]), is_left)
    elif "rotate based on" in instruction:
        new_string = rotate_based_on_pos(string, words[6])
    elif "reverse position" in instruction:
        new_string = reverse_pos_x_through_y(string, int(words[2]), int(words[4]))
    elif "move position" in instruction:
        new_string = move_pos_X_to_Y(string, int(words[2]), int(words[5]))
    else:
        print("something went wrong")
        
    return new_string




initial_password = "abcdefgh"
with open("input.txt", 'r') as f:
    A = f.read()
    
instrctions_raw = A.split("\n")

string = list(initial_password)
for instruction in instrctions_raw:
    string = decifer_instruction(string, instruction)
    print("".join(string))

solution1 = "".join(string)
print("Solution 1:", solution1)


#%% Part 2, brute force, testing all the passwords, until I find one which 
### scrambles into the searched scrambelled password

scrambled_password = "fbgdceah"
sp_list = list(scrambled_password)

perm_list = permutations(list("fbgdceah"))
for i, perm in enumerate(perm_list):
    string = list(perm)
    for instruction in instrctions_raw:
        string = decifer_instruction(string, instruction)
    if string == sp_list: ##Solution found
        break
    
solution2 = "".join(perm)
print("Solution 2", solution2)


### Comment: Since the solution is found in about 10-15 seconds on my laptop,
### I am to lacy to find the reverse solution of the scrambling process. 
### Plus: The rotation based on the position of letter X is not injectiv
