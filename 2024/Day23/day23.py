#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

from itertools import combinations

def is_connected(pc_list: list[str], connections: list[list[str, str]]) -> bool:
    for i, pc1 in enumerate(pc_list[:-1]):
        for j, pc2 in enumerate(pc_list[i+1:]):
            if sorted([pc1, pc2]) not in connections:
                return False
    return True


## Reading and parsing input
with open("input.txt", "r") as f:    
    A = f.read()
connections = [ sorted(x.split("-")) for x in  A.split("\n")]
all_pcs = set([x[0] for x in connections]+[x[1] for x in connections])
con_dict = {}
for pc in all_pcs:
    con_dict[pc] = []

    for con in connections:
        if pc in con:
            con_dict[pc] += [x for x in con if x!=pc]
        
        
## find all triplets #
all_t_triplets = []
for pc in all_pcs:
    if pc[0] != "t": # need onlty PCs starting with t
        continue
    for i, pc2 in enumerate(con_dict[pc][:-1]):
        for j, pc3 in enumerate(con_dict[pc][i+1:]):
            if sorted([pc2, pc3]) in connections:
                all_t_triplets.append([pc, pc2, pc3])
all_t_triplets = set([tuple(sorted(x)) for x in all_t_triplets])
print("Solution 1:", len(all_t_triplets))


#%%## Part 2 Looking for the largest network of interconnected PCs
## be n the size of the largest network found yet
## For each pc:
##      get the list of all PCs connected to the starting PC
##      get all possible networks which are larger than the largest network
##      found yet. Starting from largest going to smallest:
##          Check if all pcs in this test set are interconnected
##      start from the largest possible network in this list and the
##      

network_length = 3  ## there are at least triplets
for pc in all_pcs:
    test_pc_list = [pc] + con_dict[pc]
    
    search = True
    for l in range(len(test_pc_list), network_length, -1): # Only test networks which might be larger
        if not search: ## stop if already a larger network is found
            break
        ## Get all combinations of size l
        pc_combis = list(combinations(test_pc_list, l))
        for combi in pc_combis:
            if is_connected(combi, connections):
                network_length = len(combi)  ## want a larger one!
                largest_network = combi
                search = False
                break
    
res2 = ",".join(sorted(largest_network))
print("Solution 2:", res2)
        
