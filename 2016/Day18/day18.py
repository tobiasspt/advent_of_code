# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""


def get_upper_tiles(previous_row: str, index: int) ->str:
    
    if index == 0:
        upper_tiles = "."+previous_row[:2]
    elif index == len(previous_row)-1:
        upper_tiles = previous_row[-2:]+'.'
    else:
        upper_tiles = previous_row[index-1:index+2]
        
    return upper_tiles


def is_safe_pattern(upper_tiles: str) ->str:
    
    if upper_tiles == "^..":
        return "^"
    elif upper_tiles == "..^":
        return "^"
    elif upper_tiles == ".^^":
        return "^"
    elif upper_tiles == "^^.":
        return "^"
    else:
        return "."


def get_next_tile(previous_row: str, index: int) -> str:
    return is_safe_pattern(get_upper_tiles(previous_row, index))
  


def get_next_row(previous_row: str) ->str:
    new_string = ""
    for i in range(len(previous_row)):
        new_string += get_next_tile(previous_row, i)
    return new_string



#Reading the input
with open('input.txt','r') as f:    
    A = f.read()
    
# Part 1
first_row = A
n_rows = 40
rows = [first_row]
previous_row = first_row
for i in range(n_rows-1):
    previous_row = get_next_row(previous_row)
    rows.append(previous_row)
solution1 = sum([row.count(".") for row in rows])
print("Solution 1:", solution1)

#%% Part 2, Lazy brute force solution. Takes about 20 s

first_row = A
n_rows = 400000
rows = [first_row]
previous_row = first_row
for i in range(n_rows-1):
    previous_row = get_next_row(previous_row)
    rows.append(previous_row)
    
solution2 = sum([row.count(".") for row in rows])
print("Solution 2:", solution2)


