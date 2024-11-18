# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""

#Reading the input
with open('input.txt','r') as f:    
    A = f.read()
number_of_players = int(A)

import numpy as np



#%%
# number_of_players = 5
number_of_players = int(A)
list_of_players = list(np.arange(number_of_players)+1)

while len(list_of_players) > 1:
    len_start = len(list_of_players)
    list_of_players = list_of_players[::2]
    
    if len_start%2:
        list_of_players.insert(0, list_of_players[-1])
        list_of_players = list_of_players[:-1]
        
solution1 = list_of_players[0]
print("Solution 1:", solution1)



#%% Part 2
number_of_players = int(A)
list_of_players = list(np.arange(number_of_players)+1)

while len(list_of_players) > 1:
    
    length = len(list_of_players)
    number_of_steals = int(np.ceil(length/3))

    if length%2:
        start_end = int(np.ceil(length/2))  
    else:
        start_end = int(length/2)+2

    from_the_end = list_of_players[start_end::3]
    have_stolen = list_of_players[:number_of_steals]

    difference = -2*number_of_steals + length - len(from_the_end) 
    if difference:
        left_overs = list_of_players[number_of_steals:number_of_steals+difference]
    else:
        left_overs = []
        
    new_list_of_players = left_overs + from_the_end + have_stolen
    list_of_players = new_list_of_players
    
print("Solution 2:", list_of_players[0])



    
    
    
    
    
    