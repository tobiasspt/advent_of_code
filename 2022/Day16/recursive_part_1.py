# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""


global max_pressure
import numpy as np

from collections import OrderedDict

with open('input.txt', 'r') as f:
    A_input = f.read().split('\n')


valves_dict = {}
for line in A_input:
    words = line.split()
    valves_dict[words[1]] = {'rate': int(words[4].split('=')[-1].strip(';') ), 
                             'tunnels_to': [x.strip(',') for x in words[9:]]
                             }


flow_rates = [valves_dict[key]['rate'] for key in valves_dict.keys()]
names = [key for key in valves_dict.keys()]
sorted_flow_rates = np.sort(flow_rates)
sorted_names = np.array(names)
sorted_names = sorted_names[np.array(flow_rates).argsort()]

valves_ord = OrderedDict()

for r,n in zip(sorted_flow_rates, sorted_names):
    valves_ord[n] = r


functioning_valves = np.sum(sorted_flow_rates!=0)

max_steps = 30


def max_additional_achievable_preassure(steps, open_rate, open_list, max_steps=max_steps):
    """
    More sophisticated form, taking into account if the larger valves 
    are already open 
    """
    remaining = max_steps - steps
    mp = open_rate*remaining  #rate of open valves continues releasing prassure
    
    open_valves = open_list
    possible_vales = list(sorted_flow_rates)
    for o in open_valves:
        possible_vales.remove(valves_ord[o])
        
    needed = np.array(np.zeros([max_steps*2]).tolist() + possible_vales)

    i = 1
    while remaining > 0:  
        index1 = -i
   
        
        mp += needed[index1]  * remaining
        i += 1
        remaining -= 2
        
    return mp


    
#%%

global counts
global max_pressure


def recursive(steps, pos_me, camefrom_me, released_preassure, open_list, open_rate):
    global counts
    global max_pressure
    
    counts +=1
    
    if steps == max_steps:
        if released_preassure > max_pressure:
            max_pressure = released_preassure
            print(steps, released_preassure)
        return
    
    if max_additional_achievable_preassure(steps, open_rate, open_list) + released_preassure < max_pressure:
        return
    
    
    released_new = released_preassure + open_rate
    neighbours_me  = valves_dict[pos_me]['tunnels_to']
    rate_me = valves_dict[pos_me]['rate']
    
    
    # 1) I open my valve
    if rate_me != 0 and pos_me not in open_list:
        new_pos_me = pos_me
        new_open_list = open_list + [pos_me]
        new_open_rate = open_rate + valves_dict[pos_me]['rate']
        new_camefrom_me = ''

        recursive(steps+1, new_pos_me, new_camefrom_me, released_new, new_open_list, new_open_rate)

    # 2)  I move on
    for neigh in neighbours_me:
        #moving back without opening a valve is pointless
        if neigh != camefrom_me: 
            new_pos_me = neigh
            new_camefrom_me = pos_me

            recursive(steps+1, new_pos_me, new_camefrom_me, released_new, open_list, open_rate)

#%%
counts = 0
max_pressure = 0
recursive(0, 'AA', '', 0, [], 0)

print('Solution1:', max_pressure)

