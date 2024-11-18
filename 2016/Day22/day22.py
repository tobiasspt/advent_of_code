# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""

with open("input.txt", 'r') as f:
    A = f.read()    
    
    
    
nodes = A.split("\n")[2:]


def is_viable_pair(used_A: int, avail_B: int) -> bool:
    if used_A == 0:
        return False
    if  used_A <= avail_B:
        return True
    else:
        return False



node_list = []
for node in nodes:
    words = node.split()
    Size,  Used,  Avail = words [1:4]
    node_list.append([int(Size[:-1]), int(Used[:-1]), int(Avail[:-1])])
    
    
    
n_viable_pairs = 0
for i in range(len(node_list)):
    for j in range(len(node_list)):
        if i==j:
            continue
        used_A = node_list[i][1]
        avail_B = node_list[j][2]

        if is_viable_pair(used_A, avail_B):
            n_viable_pairs += 1

print("Solution 1:", n_viable_pairs)


   

#%% Part 2
"""
After trying to solve the riddle with brute force, a closer inspection of the
memory grid showed, that actually the solution is simply found by hand. 
Only the "empty" node can move. And it has to avoid the line of large nodes.
The empty node first has to reach the desired data node. 
This takes 17+3+32 steps. 

Then the desired data has to be moved left max_x -1 times. Each 

"""


node_dict = {}
for node in nodes:
    
    words = node.split()
    name = words[0]
    coords = name.split('-')[1:]
    xcoord = int(coords[0][1:])
    ycoord = int(coords[1][1:])
    Size,  Used,  Avail = words [1:4]

    node_dict[(xcoord, ycoord)] = {'name': name, "size": int(Size[:-1]),
                                   'used': int(Used[:-1]),
                                   'avail':int(Avail[:-1]),
                                   }

max_x = max([x[0] for x in node_dict.keys()])
max_y = max([x[1] for x in node_dict.keys()])
n_nodes = (max_x+1) * (max_y+1)




import numpy as np
import matplotlib.pyplot as plt

memory_nodes = np.zeros([max_x+1, max_y+1])

for y in range(max_y+1):
    for x in range(max_x+1):
        memory_nodes[x,y]  = node_dict[(x,y)]["used"]


memory_nodes = memory_nodes.transpose()

plt.figure(dpi=300)
plt.imshow(memory_nodes)
plt.colorbar()
plt.plot(0,0,'rx', label="node 00")
plt.plot(max_x,0,'yx', label="data")
plt.legend(loc='lower right')
plt.title('used memory')
        

"""
After trying to solve the riddle with brute force, a closer inspection of the
memory grid showed, that actually the solution is simply found by hand. 
Only the "empty" node can move. And it has to avoid the line of large nodes.
The empty node first has to reach the desired data node. 
This takes 17+3+32 steps. 

Then the desired data has to be moved left max_x-1 times. Each of these 
movements takes 5 memory shifts. 
"""
        
solution2 = 17+3+32 + (max_x-1)*5
print("Solution 2 by hand:", solution2)


#%%


# the state hash is a tuple of 2 tuples. 
# th2 two tuples represent the coordinates of
# 1) the empty node
# 2) the target data

from collections import defaultdict
from functools import lru_cache

@lru_cache
def neighbours(coords: tuple[int, int], max_x: int, max_y: int) -> list[tuple[int, int]]:
    x,y = coords
    neighs=[]
    if x > 0:
        neighs.append((x-1, y))
    if x < max_x:
        neighs.append((x+1, y))
    if y > 0:
        neighs.append((x, y-1))
    if y < max_y:
        neighs.append((x, y+1))
    return neighs
    
    

state_hash_dict = defaultdict(lambda: 10000)


start_data = (max_x, 0)

for coords in node_dict.keys():
    if node_dict[coords]['used'] == 0:        
        start_empty = coords



min_steps = 500  #educaed guess


def handle_state(cs: tuple[tuple[int, int]] , steps: int) -> None:
    global min_steps 

    if steps >= min_steps:
        return
    
    empty = cs[0]
    data = cs[1]
    
    if data == (0,0):
        ## we are at the end
        if steps < min_steps:
            min_steps = steps
            print("min_steps", min_steps)
        return
        
    ##check if the same state is already visited
    if steps >= state_hash_dict[cs]:
        return
    else:
        state_hash_dict[cs] = steps
    
    neighs = neighbours(empty, max_x, max_y)
    for nn in neighs:
        if node_dict[empty]["size"] >= node_dict[nn]["used"]:
            new_empty = nn
            
            if nn == data:
                new_data = empty
            else:
                new_data = data
                
            new_state = (new_empty, new_data)
            if steps +1 >= state_hash_dict[new_state]:
                continue
                
            handle_state(new_state, steps+1)
       
handle_state((start_empty, start_data), 0)
print("Solution 2", min_steps)
    
    
