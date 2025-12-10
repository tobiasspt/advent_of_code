#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

from collections import defaultdict

def decode_molecule(molecule: str) -> list[str]:
    molecule_list = []
    for char in molecule:
        if char.isupper():
            molecule_list.append(char)
        else:
            molecule_list[-1] = molecule_list[-1] + char
    return molecule_list


with open("input.txt", "r") as f:    
    A = f.read()
replacements, initial_molecule = A.split("\n\n")

replacement_dict = defaultdict(lambda: [])
for replacement in replacements.split("\n"):
    start, end = replacement.split(" => ")
    end = decode_molecule(end)
    replacement_dict[start].append(end)


list_of_possibilities = []
initial_molecule_list = decode_molecule(initial_molecule)
for i, element in enumerate(initial_molecule_list):
    start = initial_molecule_list[:i]
    end = initial_molecule_list[i+1:]
    for replacement in replacement_dict[element]:
        list_of_possibilities.append("".join(start+replacement+end))
           
res1 = len(set(list_of_possibilities))
print("Solution 1:", res1)
    

#%% part 2
"""
The second part took me way too long for the simple solution I came up with. 
First I tried to solve the second part, by solving each possibility and smart
caching and reducing of duplicate solution. 

At the end an accuarate look at the replacements showed a rather easy solution. 
There are replacements, where from 1 element, 2 elements are created. 
And other replacements, where from 1 element, a sequence of fore or more 
elements are created. In the longe sequences appears always a pair or elements, 
which do not appear elsewhere. In between these, a few combinations are alowed.
One element appears only in between these "pair" elements and cannot be created
otherwise. (I dub it element M)
It happens to be that if there is 2 of this element in a pair, the long sequence
is 8 elements long. If one is in the pair - 6 long, if none is in the pair 
- 4 long. 

So starting from the final molecule, replace all pairs in the correct order. 
And count, how many of these element M are in each pair. So one can figure out
the minimum amount of replacements needed. 
"""


molecule_list = decode_molecule(initial_molecule)

steps = 0
while "Ar" in molecule_list:

    pos_Ar = molecule_list.index("Ar")
    pos_Rn = [i for i, x in enumerate(molecule_list) if x == "Rn"]
    pos_Rn = [x for x in pos_Rn if x < pos_Ar]
    index_end = pos_Ar
    index_start = pos_Rn[-1]
    
    
    count_Y = molecule_list[index_start:index_end].count("Y")
    if count_Y == 2:
        extra = 4
    elif count_Y == 1:
        extra = 2
    elif count_Y == 0:
        extra = 0


    elements_in_between = len(molecule_list[index_start+1:index_end])
    steps_for_in_between = elements_in_between - extra
    steps += steps_for_in_between
    
    for i in range(index_start - 1, index_end+1):
        molecule_list[i] = []
    molecule_list[index_start -1 ]  = "X"
    molecule_list = [x for x in molecule_list if x != []]
    
res2 = steps + len(molecule_list) - 1
print("Solution 2:", res2)
    

