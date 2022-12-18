# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

with open('input.txt', 'r') as f:
    A_input = f.read()
    
gas = list(A_input)

# # Testinput
# gas = list('>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>')

len_gas = len(gas)

#shapes
"""
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""



#Rock gets first pushed left or right; than down

# Shape appears:
# left edge is two blocks asway from left wall
# lowest block is 3 blocks away from floor or highest block

def new_center(y_max):
    x_center = 2
    y_center = y_max + 4   
    return (x_center, y_center)


def shape(shape_number, pos):
    
    if shape_number == 0:
        shape_list = {(x+pos[0], pos[1]) for x in range(4)}
        
    elif shape_number == 1:
        shape_list = {(x+pos[0], pos[1]+1) for x in range(3)}
        shape_list.add( (1+pos[0], pos[1]+2))
        shape_list.add( (1+pos[0], pos[1]-0))
        
    elif shape_number == 2:
        shape_list = {(x+pos[0], pos[1]) for x in range(3)}
        shape_list.add((2+pos[0], pos[1]+1))
        shape_list.add((2+pos[0], pos[1]+2))
        
    elif shape_number == 3:
        shape_list = {(pos[0], pos[1]+y) for y in range(4)}
        
    elif shape_number == 4:
        shape_list = {(pos[0], pos[1]), (pos[0], pos[1]+1), (pos[0]+1, pos[1]), (pos[0]+1, pos[1]+1)}
        
    return shape_list
            


def bottom_contact(pos_shapes, stopped_shapes ):
    #Hitting bottom
    for block in pos_shapes:
        if block in stopped_shapes:
            return True
    else:
        return False

    
    

def side_contact(pos_shapes, stopped_shapes ):
    #Hitting wall
    shape_x = {x[0] for x in pos_shapes}
    if min(shape_x) < 0 or max(shape_x) > 6:
        return True
    
    #Hitting bottom or side
    for block in pos_shapes:
        if block in stopped_shapes:
            return True
        
    else:
        return False


def move_down(pos_shapes, stopped_shapes):
    pos_shapes_new = {(x[0], x[1]-1) for x in pos_shapes}

    if not bottom_contact(pos_shapes_new, stopped_shapes):
        return pos_shapes_new, False
    
    else:
        return pos_shapes, True
    
    
def move_sideways(pos_shapes, gas_inst, stopped_shapes):
    
    if gas_inst == '>':
        dx = 1
    elif gas_inst == '<':
        dx = -1
    
    pos_shapes_new = {(x[0]+dx, x[1]) for x in pos_shapes}
    
    if not side_contact(pos_shapes_new, stopped_shapes):
        return pos_shapes_new, False
    
    else:
        return pos_shapes, True    
    
def move_new_rock(shape_number, gas_index, stopped_shapes, ymax, i):
    
    pos_shapes = shape(shape_number, new_center(ymax))
        
    while True:        
        gas_inst = gas[gas_index]
        gas_index  = (gas_index+1)%len_gas
        
        pos_shapes, hit = move_sideways(pos_shapes, gas_inst, stopped_shapes)        
        pos_shapes, hit_down = move_down(pos_shapes, stopped_shapes)
        
        if hit_down:
            break
        
    y_max_new =   max({x[1] for x in pos_shapes})
    
    if y_max_new > ymax:
        ymax = y_max_new
    
    stopped_shapes = stopped_shapes.union(pos_shapes)
    
    return gas_index, stopped_shapes, ymax



#%% Part1


gas_index = 0 
shape_number = 0
stopped_shapes = set((x,0) for x in range(7))

ymax = 0
remove = 250
for i in range(2022):
    gas_index, stopped_shapes, ymax = move_new_rock(shape_number, gas_index, stopped_shapes, ymax, i)
    shape_number = (shape_number+1)%5
    
    if not i%remove:
        max_y = max({x[1] for x in stopped_shapes})
        stopped_shapes = {x for x in stopped_shapes if (max_y - x[1]) < remove}


print(ymax) 
