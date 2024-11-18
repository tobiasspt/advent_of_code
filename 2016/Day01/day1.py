# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""
import numpy as np

#Reading the input
with open('input.txt','r') as f:    
    instructions = f.read()

# Part 1
i_list = instructions.split(',')

# Facing in which direction
# N=0, E=1, S=2, W=3
face = 0
posx = 0
posy = 0

for inst in i_list:
    inst = inst.strip()
    dist = int(inst[1:])
    
    if inst[0] == 'R':
        face+=1
        face = face%4
    elif inst[0] == 'L':
        face-=1
        face = face%4
    else:
        print('error')
        
    if face == 0:
        posx += dist
    elif face == 1:
        posy += dist
    elif face == 2:
        posx -= dist
    elif face == 3:
        posy -= dist
    else: 
        print('error')
        
sol1 = np.abs(posx)+np.abs(posy)
print('Solution part 1:', sol1)


#Part 2
i_list = instructions.split(',')

# Facing in which direction
# N=0, E=1, S=2, W=3
face = 0
posx = 0
posy = 0

locations = [(0,0)]
inst_ind = 0
hq_not_found = True

while hq_not_found:
    inst = i_list[inst_ind].strip()
    dist = int(inst[1:])
    
    if inst[0] == 'R':
        face+=1
        face = face%4
    elif inst[0] == 'L':
        face-=1
        face = face%4
    else:
        print('error')
        
    for i in range(dist):    
        if face == 0:
            posx += 1
        elif face == 1:
            posy += 1
        elif face == 2:
            posx -= 1
        elif face == 3:
            posy -= 1
        else: 
            print('error')
        
        new_pos=(posx, posy)
        if new_pos in locations:
            hq_not_found=False
            break
        else:
            locations.append(new_pos)
    inst_ind += 1
    
sol1 = np.abs(posx)+np.abs(posy)
print('Solution part 2:', sol1)