#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

with open("input.txt", "r") as f:    
    A = f.read()

lines = A.split("\n")

"""
x is the first index, 
y is the second index
"""


def get_neighbours(num):
    index, length, y = number_dict[num]
    neighbours = set()
    neighbours.add((index-1, y))
    neighbours.add((index+length, y))
    for i in range(length+2):
        neighbours.add((index+i-1, y+1))
        neighbours.add((index+i-1, y-1))
    return neighbours


digits = [str(x) for x in range(0,10)]
number_dict = {}
symbol_set = set()
gear_set = set()

counter = 0

for y, line in enumerate(lines):
    ix = 0
    while ix < len(line):
        x = line[ix]
        if x == ".":
            ix += 1
            continue
        elif x not in digits:
            symbol_set.add((ix, y))
            if x == "*":
                gear_set.add((ix, y))
            ix += 1
            
        else:
            num = x
            ix += 1
            while True:
                if ix < len(line) and line[ix] in digits:
                    num += line[ix]
                    ix += 1
                else:
                    break
                
            index = ix - len(num) 
            
            # Avoiding double naming
            name = num+'_'+str(y)
            while name in number_dict:
                name += "."
            number_dict[name] = (index, len(num), y)
        
        
# Solution 1
res1 = 0
for num in number_dict.keys():
    neighs = get_neighbours(num)
    check = sum([1 for neigh in neighs if neigh in symbol_set])
    if check > 0:
        res1 += int(num.split('_')[0])
print(f"Solutoin 1:\n{res1}")


#%% Part 2
 
gear_dict = {}
for gear in gear_set:
    gear_dict[gear] =[]

for num in number_dict.keys():
    neighs = get_neighbours(num)
    for gear in gear_set:
        if gear in neighs:
            gear_dict[gear].append(int(num.split('_')[0]))
            
res2 = 0
for gear in gear_dict:
    if len(gear_dict[gear]) == 2:
        res2 += gear_dict[gear][0] *  gear_dict[gear][1]

print(f"Solution 2:\n{res2}")
