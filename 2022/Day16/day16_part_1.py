# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np

with open('input.txt', 'r') as f:
    A_input = f.read().split('\n')

valves_dict = {}

for line in A_input:
    words = line.split()
    
    valves_dict[words[1]] = {'rate': int(words[4].split('=')[-1].strip(';') ), 
                             'tunnels_to': [x.strip(',') for x in words[9:]]
                             }


names = [key for key in valves_dict.keys()]
flow_rates = [valves_dict[key]['rate'] for key in valves_dict.keys()]

state = {'steps': 0, 'pos': 'AA', 'p_released': 0, 'open': [], 'camefrom': ''}




def preassure_release_min(state):
    return np.sum([valves_dict[valve]['rate'] for valve in state['open']])
        

def explore_state(state):
    
    new_states = []
    
    pos = state['pos']
    neighbours = valves_dict[pos]['tunnels_to']
    rate = valves_dict[pos]['rate']
    
    new_release = preassure_release_min(state)
    
    #open the valve
    if rate != 0 and pos not in state['open']:
        new_states.append({'steps': state['steps'] +1,
                           'pos': pos,
                           'p_released': state['p_released'] + new_release,
                           'open': state['open'] + [pos],
                           'camefrom': ''})

    for neigh in neighbours:
        
        #moving back without opening a valve is pointless
        if neigh != state['camefrom']: 
        
            new_states.append({'steps': state['steps'] +1,
                               'pos': neigh,
                               'p_released': state['p_released'] + new_release,
                               'open': state['open'].copy(), 
                               'camefrom': pos})

    return new_states, state['p_released']



new_states = [state]


sorted_flow_rates = np.sort(flow_rates)

def max_achievable_preassure(state, max_steps=30):
    
    mp = 0
    steps = state['steps']
    remaining = max_steps - steps
    mp += preassure_release_min(state)*remaining
    i = 1
    while remaining > 0:
        mp += sorted_flow_rates[-i] * remaining
        i += 1
        remaining -= 2
    
    return mp
    



max_preassure = 0
completed = 0
counter = 0

while len(new_states) != 0:
    counter += 1
    
    if new_states[-1]['steps'] == 30:
        completed += 1
        newp = new_states[-1]['p_released']
        if newp > max_preassure:
            max_preassure = newp
            print(max_preassure, completed)
        new_states.pop()
    
    elif new_states[-1]['p_released'] + max_achievable_preassure(new_states[-1]) < max_preassure:
        new_states.pop()
    
    else:
        
        new, p = explore_state(new_states[-1])
        new_states.pop()
        new_states += new
    

print('Solution1:', max_preassure, counter)