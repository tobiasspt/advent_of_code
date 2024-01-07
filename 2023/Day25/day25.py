#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import copy
from collections import defaultdict

"""
My Ansatz:
Loop over all connected pairs. 
Select one of the components and check how long it takes to get to the second
component.  
If this path is longer than a certain threshold, this connection is the one
to be cut. 
"""

def get_connected_group(start_component: str, already_in_group: set, comp_dict: dict) -> set:
    """
    Finds all components which are connected to the start_component.
    It is a recursive function. 
    """
    already_in_group.add(start_component)
    next_comp = [x for x in comp_dict[start_component] if x not in already_in_group]
    
    for x in next_comp:
        new_already = get_connected_group(x, already_in_group, comp_dict)
        already_in_group = already_in_group.union(new_already)
        
    return already_in_group


with open("input.txt", "r") as f:    
    A = f.read()
pairs = []
for line in A.split("\n"):
    first, others = line.split(":")
    for other in others.split(" "):
        if other == "":
            continue
        pairs.append([first, other])
        
comp_dict = defaultdict(lambda: [])
for pair in pairs:
    comp_dict[pair[0]].append(pair[1])
    comp_dict[pair[1]].append(pair[0])


max_len = 10
    
connections_to_cut = []
for start in comp_dict.keys(): # looping over all possible starts

    for first_connection in comp_dict[start]:
        paths = [[start, first_connection]]
        
        is_short = False
        
        while not is_short > 0 and len(paths) > 0:

            p = paths.pop(0)
            current_pos = p[-1]
            
            if len(p) > max_len:
                continue
            
            neighs = comp_dict[current_pos]
            neighs = [x for x in neighs if x  !=p[-2] ] #dont go back where I came from
            
            for n in neighs:
                if n == start:
                    is_short = True
                    break
                if n in p:
                    continue
                else:
                    new_p = copy.copy(p)
                    new_p.append(n)
                    paths.append(new_p)
                    
        if not is_short:
            connections_to_cut.append([start, first_connection])
 
        

p = copy.deepcopy(comp_dict)
indices = []

for con in connections_to_cut:
    
    if con in pairs:
        indices.append(pairs.index(con))
    
i, j, k = indices
        

p[pairs[i][0]].remove(pairs[i][1])
p[pairs[j][0]].remove(pairs[j][1])
p[pairs[k][0]].remove(pairs[k][1])

p[pairs[i][1]].remove(pairs[i][0])
p[pairs[j][1]].remove(pairs[j][0])
p[pairs[k][1]].remove(pairs[k][0])

group1 = get_connected_group(pairs[0][0], set(), p)
result = len(group1) * ( len(comp_dict) - len(group1) )
print(f"Solution 1\n{result}")





    